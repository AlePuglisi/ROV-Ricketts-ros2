# ROV-Ricketts-ros2
Underwaater World Simulation | ROV | ROS2 Jazzy | Gazebo Harmonic | 

I started this project to learn how to set up an underwater world simulation with ROS2 and Gazebo. <br/>
Gazebo Classic has reached its end of life, and it is time to learn how to use Gazebo sim. <br/>

Thanks to the huge amount of available models gifted by MBARI on [sketchfab](https://sketchfab.com/search?q=mbari&type=models), my objective is to: 
- Create a URDF Model of MBARI's  [ROV Doc Ricketts](https://www.mbari.org/technology/rov-doc-ricketts/)
   - Model each thruster as an independent joint
   - Model and Integrate the actuated ROV's Manipulator (with all joints) 
- Define an approximated fluid dynamic model of the ROV, for simulation
- Learn to correctly set up Gazebo sim plugins to simulate thrusters, buoyancy, and Fluidodinamic force
- Create a custom sdf world file, with deep-sea environments from MBARI's 3D floor reconstruction 
- Add deep sea creatures as [Gazebo Actors](https://gazebosim.org/docs/latest/actors/), to make this world even more alive.
  This is possible thanks to [Photogrammetry Techniques](https://www.mbari.org/wp-content/uploads/Kaiser_Nicole.pdf) used by MBARI.
- 
