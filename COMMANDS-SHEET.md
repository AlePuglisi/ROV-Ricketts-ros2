# ROV-Ricketts-ros2 | COMMAND SHEET 
**Unofficial MBARI's ROV Simulation and Control Project** <br/>
Underwater World Simulation | ROV | ROS2 Jazzy | Gazebo Harmonic | 

<image width=450 heigth=300 src=https://github.com/user-attachments/assets/5a26e743-ca25-4e6b-828f-766e30c5d696>
  
### Clone this repository and build 
Move to your ros workspace, inside /src folder (where all your packages are located) 
```
# Terminal
git clone https://github.com/AlePuglisi/ROV-Ricketts-ros2.git
```

### Terminal Commands to launch visualization/simulation/control
- Visualize Ricketts **with the Robotic Arm** in Rviz: 
  ```
  # Terminal
  ros2 launch rov_ricketts_description display.launch.py load_arm:=true
  ```
- Visualize Ricketts **without the Robotic Arm** in Rviz: 
  ```
  # Terminal
  ros2 launch rov_ricketts_description display.launch.py load_arm:=false
  ```
  Or simply (being the default configuration set to ``false``): 
  ```
  # Terminal
  ros2 launch rov_ricketts_description display.launch.py 
  ```

