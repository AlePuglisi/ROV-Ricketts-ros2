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

## 1.2. Set up empty underwater World Gazebo Harmonic Simulation

## 1.3. Tune Thrusters, Buoyancy, and other fluid dynamic Plugins for the ROV Model 

## 1.4. Spwan and Move ROV Ricketts in the empty world

## 1.5. Include 

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

