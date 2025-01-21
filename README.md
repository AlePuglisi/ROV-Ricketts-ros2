# ROV-Ricketts-ros2
**Unofficial MBARI's ROV Simulation and Control Project** <br/>
Underwater World Simulation | ROV | ROS2 Jazzy | Gazebo Harmonic | 

<image width=450 heigth=300 src=https://github.com/user-attachments/assets/5a26e743-ca25-4e6b-828f-766e30c5d696>

I started this project because of my interest in underwater robotics and fascination with the [MBARI](https://www.mbari.org/) Oceanographic Institute. <br/>

During this project, I want to learn how to set up an underwater world simulation with ROS2 and Gazebo. <br/>
Gazebo Classic has reached its end of life, and it is time to learn how to use Gazebo sim. <br/>
Due to some limitations of Gazebo, soon, I want to explore other robotics simulators, like [NVIDIA Omniverse IsaacSim](https://docs.omniverse.nvidia.com/isaacsim/latest/index.html). 

### Final (long-term) Objective
Thanks to the huge amount of available models of ROV, Environments, and Creatures gifted by MBARI on [sketchfab](https://sketchfab.com/search?q=mbari&type=models), I want to: 
- Create a URDF Model of MBARI's  [ROV Doc Ricketts](https://www.mbari.org/technology/rov-doc-ricketts/)
   - Model each thruster as an independent joint
   - Model and Integrate the actuated ROV's Manipulator (with all joints) <br/>
     (Even If currently Ricketts has 2 arms for advanced manipulation tasks, I will consider this only in the future) 
- Define an approximated fluid dynamic model of the ROV, for simulation
- Learn to correctly set up Gazebo sim plugins to simulate thrusters, buoyancy, and fluid dynamics force
- Create a custom sdf world file, with deep-sea environments from MBARI's 3D sea floor reconstruction 
- Add deep sea creatures as [Gazebo Actors](https://gazebosim.org/docs/latest/actors/), to make this world even more alive. <br/>
  This is possible thanks to [Photogrammetry Techniques](https://www.mbari.org/wp-content/uploads/Kaiser_Nicole.pdf) used by MBARI.
- Implement high and low-level ROS nodes to control and teleoperate the ROV motion (exploiting the 7 thrusters) 
- Implement high and low-level ROS nodes to control and teleoperate the ROV Arm (including Gripper operations)
- Add light sources, cameras, and other exteroceptive/proprioceptive sensors to the Robot Model. 
- Implement control on Pan-Tilt Camera motion
- Set up needed TFs, sensors, topics, and odometry to Enable Mapping with SLAM
- Set up Autonomous Navigation Features
- Implement high-level algorithms for Visual Tracking of deep water animals <br/>
  (Due to Gazebo's Limitations in rendering camera images, this may require moving to IsaacSim)
- Implement high-level algorithms for Visual Servo Control of the ROV Robotic Arm.
- ...

> [!TIP]
> The following steps can be useful for anyone who wants to create a Robotic Simulation from the robot mesh! <br/>
> Here world and robot plugins will be underwater specific, but the high-level concepts remain the same even for a ground vehicle. <br/>
> This is why I'll try to describe the implementation step as clearly as possible.<br/>
> Later on I will provide a concise command sheet to run the simulation and use its functionalities. 


... This is a lot just for a single person, :raised_hand_with_fingers_splayed: a big high five to anyone opening an issue for suggestions, ideas, or reviews. <br/>
Feel free to [Pull Requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) to contribute to this project. <br/>

This emoji " :point_right: "Indicates the current step in development. 

## Step 0. Install and Set up ROS2 + Used ROS Packages 
### Prerequisite
- Linux Ubuntu 24.04 
- ROS2 Jazzy
> [!NOTE]
> Alternatively, you can build a ``Docker`` container to work with ROS2 Jazzy in your OS.<br/>
> If you are using Docker, refer to this section just to know the required dependencies.

<details> 
<summary> Install and Set Up ROS2 Jazzy </summary>
   
- **Install** ROS Jazzy and source 
Refer to [ros documentation](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html) for the step-by-step installation tutorial. <br/>

Anytime you open a new terminal, you should source your underlay ros environment with:
```
# Terminal
# Replace ".bash" with your shell if you're not using bash
# Possible values are: setup.bash, setup.sh, setup.zsh
source /opt/ros/jazzy/setup.bash
```
To avoid doing it every time, add that command to your ``bashrc``, opening it with a text editor of your choice:
```
# Terminal (use your preferred text editor tool)
gedit ~/.bashrc
```
And add the line ``source /opt/ros/jazzy/setup.bash`` at the end.

- If not automatically installed, **install ``colcon``**, the build tool for ROS2: 
```
# Terminal
sudo apt install python3-colcon-common-extensions
```

- Create and build a **ros2 workspace** to position this project packages:<br/>
In your preferred directory
```
# Terminal
mkdir ros2_ws
cd ros2_ws
mkdir src
colcon build
```

- **Source** your ros2 workspace and the colcon argmícomplete environment:<br/>
As done for the ros underlay, you need to source the overlay setup.bash when you build it, again you can add that to the bashrc
```
# Terminal
gedit ~/.bashrc
```
Add the line ``source ~/ros2_ws/install/setup.bash`` <br/>
and ``source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash`` to complete colocn commands by pressing Tab.

### Install Additional Packages
To launch this project packages, you may need ROS2 packages not installed with ros-jazzy-desktop. <br/>
I will update this list during implementation:

- ``xacro``
- ``joint_state_publisher_gui``
- ...

```
# Terminal
sudo apt install ros-jazzy-xacro ros-jazzy-joint-state-publisher-gui 
```
</details>

### Clone this repository and build 
Move to your ros workspace, inside /src folder (where all your packages are located) 
```
# Terminal
git clone https://github.com/AlePuglisi/ROV-Ricketts-ros2.git
```
then, move back to the workspace folder (before /src), and build your workspace.<br/>
Now you are ready to test this project!<br/>
(Remember that after building the workspace, you need to source your bashrc, so your overlay and underlay will be sourced, just run ``source ~/.bashrc``)

## :point_right: Step 1. Set up The Simulation

## 1.1. Create ROV Ricketts URDF from Sketchfab Model
- First I download [Doc Ricketts ROV](https://sketchfab.com/3d-models/doc-ricketts-rov-def365ad47894a06b5f0fb2876795bf9) model from Sketchfab, in ``fbx`` format.
- Import it in Blender to create separate meshes (with texture) for each piece
- Export each model as ``dae`` (COLLADA format)<br/>

> [!TIP]
> I discovered that ``stl `` format does not support texture by default, setting it up may be possible but hard. <br/>
> [Here](https://github.com/AlePuglisi/ROV-Ricketts-ros2/tree/main/rov_ricketts_description/meshes/stl) you can find stl models, but for an astonishing visualization, rely on ``dae``.<br/>
> With the COLLADA format, textures are easy to load (just be sure the texture png file is in the correct referenced path inside dae XML file). 

- Create the ``URDF`` connecting and positioning each thruster, as a revolute joint (probably continuous joint will be used later on). <br/>
I used the ``xacro`` format, to make it cleaner and allow a simple customization at launch time. 
- Inertia property tuning will be done later on when setting up Gazebo simulation
- Creta a simple launcher [``display.launch.py``](https://github.com/AlePuglisi/ROV-Ricketts-ros2/blob/main/rov_ricketts_description/launch/display.launch.py) to run Rviz, robot_state_publisher, joint_state_publisher (and its GUI).
- Add relevant visualization objects in Rviz and save as [`` rov_monitor.rviz`` ](https://github.com/AlePuglisi/ROV-Ricketts-ros2/blob/main/rov_ricketts_description/config/rov_monitor.rviz). 

Finally, it is possible to visualize the robot in Rviz and move the thrusters with joint_state_publisher_gui: <br/>
```
# Terminal
ros2 launch rov_ricketts_description display.launch.py
```

<image src=https://github.com/user-attachments/assets/cbda4232-3072-4fbb-bc24-a6344e62501a>
   

The next step is to model and attach the robotic arm to Doc Ricketts.<br/>

##  1.2. Add ROV Manipulator to the URDF Model 
The arm is defined as a single piece in the 3D model, three options are possible to derive the URDF model:
- [ ] 1. Remodel it with simple cylinders and parallelepiped shapes, connected by revolute joints, directly in URDF.
- [ ] 2. Create a new 3D model from scratch, with separate links, using the original arm as a reference
- [x] 3. Use the original model and modify it to cut the links, then use this as URDF links

<br/>
<image src=https://github.com/user-attachments/assets/c58b649c-45cf-4ff8-883d-6c081f94382e>

   
I found the information about the robotic arm on [this interesting video](https://www.youtube.com/watch?v=BTdeXxaGfAs&t=303s&ab_channel=MBARI%28MontereyBayAquariumResearchInstitute%29) about ROV technologies at MBARI.<br/>
Thank you very much, Benjamin Erwin :pray:. <br/>
ROV Doc Ricketts is equipped with two robotic arms: 
- **Shilling TITAN 4 Manipulaotr** (T4): Strong arm, for heavy work but less precise.
- Aluminum Arm: very dexterous, for precise manipulation. 

I only modeled the [T4 manipulator](https://www.technipfmc.com/media/hpkjrigr/titan-4-datasheet.pdf),  available in the 3D Model. <br/>
 (In the URDF, I include the **arm_tool** frame, because this will help when performing manipulation tasks.)

> [!TIP]
> A useful tag to define gripper joints is "mimic": <br/>
>
>     <joint name="${name}_link4_claw_left" type="revolute">
>     <mimic joint="${name}_link4_claw_right" multiplier="1" offset="0"/>
>     ....
> 
> This forces this joint to move around its rotation axis as the mimic joint times the multiplier.<br/>
> (joint_state = mimic_joint_state * multiplier) <br/>
> Changing the multiplier value we can set an inverse rotation or a transformation ratio. 

Once Doc Ricketts Arm URDF has been derived, to make the robot reconfigurable at launch time, we can decide at launch time if we want to load it or not. <br/>
To achieve this flexibility feature, we can use a launch argument, and the xacro conditional statement. <br/>

- To configure Ricketts **with the Robotic Arm**: 
```
# Terminal
ros2 launch rov_ricketts_description display.launch.py load_arm:=true
```
- To configure Ricketts **without the Robotic Arm**: 
```
# Terminal
ros2 launch rov_ricketts_description display.launch.py load_arm:=false
```
(Notice that the default value of load_arm is false, so argument initialization can be neglected in that case)

As can be seen, all joints have been articulated properly! <br/>
Brief **Joint actuation Demo**:mechanical_arm:: 

<image src=https://github.com/user-attachments/assets/5c3c9c66-c7f4-4276-957b-2d1cf4b8ae2d>

Joint limits and dynamic joints/body properties will be defined in the next steps...

## 1.3. Tune Model Inertia parameters
Inertia parameters are fundamental for setting up Gazebo simulation. <br/>

- **TITAN 4** MANIPULATOR: 
From the manipulator's datasheet, it is possible to extract accurate information about its characteristics.<br/>
Some of them will be useful to set torque limitations and other control-related aspects, for now, let's focus on inertial properties. <br/>

 For a reliable simulation in Gazebo, we have to define the mass, inertia matrix, and center of mass position of each link. <br/>
 To extract these numbers, we can use the information about the **arm material** which is primarily Titanium (as the name suggests). <br/>
 Using Titanium density we can then use the mesh volume to compute mass and some software resources to compute CoM position and Inertia matrix automatically.  


## 1.4. Set up an empty underwater World in Gazebo Harmonic

## 1.5. Add and Tune Buoyancy, fluid dynamic, and thruster Gazebo sim plugins

## 1.6. Move ROV Ricketts in an Empty Gazebo World



## Step 2. Create Gazebo Deep Sea World from Sketchfab Models

## 2.1. Import and Position desired environmental deep-sea elements

## 2.2. Import deep-sea creatures meshes

## 2.3. Define "Actor" Behaviours for animals

## Step 3. Set Up Robot Teleoperation

## 3.1. Map Desired motion in free space to thruster commands

## 3.2. Implement Teleoperation Node

## 3.3. Map Joystick or CLI commands to correct thrusters command

## Step 4. Set Up Arm Teleoperation 

## 4.1. Rely on the Teleoperation Node to include new arm-related commands

## 4.2. Use Movit2 or ros2_control for Joint Control of the Arm 

## Step 5 and so on ... 

