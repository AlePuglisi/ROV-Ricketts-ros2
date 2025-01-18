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
- Learn to correctly set up Gazebo sim plugins to simulate thrusters, buoyancy, and Fluidodinamic force
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

This emoji " :point_right: " Indicate the current step in development. 

## Step 0. Install and Set up ROS2 + Used ROS Packages 
... WIP ... 

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

<image heigth=400 width=688 src=https://github.com/user-attachments/assets/cbda4232-3072-4fbb-bc24-a6344e62501a>
   

The next step is to model and attach the robotic arm to Doc Ricketts.<br/>

##  1.2. Add ROV Manipulator to the URDF Model 
The arm is defined as a single piece in the 3D model, three options are possible to derive the URDF model:
- [ ] 1. Remodel it with simple cylinders and parallelepiped shapes, connected by revolute joints, directly in URDF.
- [ ] 2. Create a new 3D model from scratch, with separate links, using the original arm as a reference
- [x] 3. Use the original model and modify it to cut the links, then use this as URDF links

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

## 1.3. Set up empty underwater World in Gazebo Harmonic

## 1.4. Tune Links Inertia, Buoyancy, fluid dynamic Plugins, and Thrusters for the ROV Model 

## 1.5. Move ROV Ricketts in an Empty Gazebo World



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

