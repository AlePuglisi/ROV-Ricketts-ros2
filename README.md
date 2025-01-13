# ROV-Ricketts-ros2
Underwater World Simulation | ROV | ROS2 Jazzy | Gazebo Harmonic | 

I started this project to learn how to set up an underwater world simulation with ROS2 and Gazebo. <br/>
Gazebo Classic has reached its end of life, and it is time to learn how to use Gazebo sim. <br/>

### Final (long-term) Objective
Thanks to the huge amount of available ROV, Environments, and Creatures models gifted by MBARI on [sketchfab](https://sketchfab.com/search?q=mbari&type=models), I want to: 
- Create a URDF Model of MBARI's  [ROV Doc Ricketts](https://www.mbari.org/technology/rov-doc-ricketts/)
   - Model each thruster as an independent joint
   - Model and Integrate the actuated ROV's Manipulator (with all joints)
- Define an approximated fluid dynamic model of the ROV, for simulation
- Learn to correctly set up Gazebo sim plugins to simulate thrusters, buoyancy, and Fluidodinamic force
- Add light sources, cameras, and other exteroceptive/proprioceptive sensors to the Robot Model. 
- Create a custom sdf world file, with deep-sea environments from MBARI's 3D floor reconstruction 
- Add deep sea creatures as [Gazebo Actors](https://gazebosim.org/docs/latest/actors/), to make this world even more alive. <br/>
  This is possible thanks to [Photogrammetry Techniques](https://www.mbari.org/wp-content/uploads/Kaiser_Nicole.pdf) used by MBARI.
- Implement high and low-level ROS nodes to control and teleoperate the ROV motion (exploiting the 7 thrusters) 
- Implement high and low-level ROS nodes to control and teleoperate the ROV Arm (including Gripper operations)
- Implement control on Pan-Tilt Camera motion
- Set up needed TFs, sensors, topics, and odometry to Enable Mapping with SLAM
- Set up Autonomous Navigation Features
- Implement high-level algorithms for Visual Tracking of deep water animals <br/>
  (Due to Gazebo's Limitations in rendering camera images, this may require moving to IsaacSim)
- Implement high-level algorithms for Visual Servo Control of the ROV Robotic Arm.
  
... This is a lot just for a single person, create an issue for any suggestion, idea, or review. <br/>
Feel free to [Pull Requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) to contribute to this project.


