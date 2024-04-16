# xbox-haptic

This repository is to give haptic feedback by vibration to your controller which is connected to the force sensor at the manipulator

At the end, terminal should look similar to following:
[haptic](https://github.com/kenanalperen/xbox-haptic/blob/main/haptic.jpg)

First run ros1, ros2 and bridge them. (follow below link)

[ROS1-ROS2 Bridge](https://github.com/kenanalperen/ros1-2)

# Initial steps for getting the force data to ROS2
Subscribe to the moca force sensor data in ROS1 (or alternatively rosbag) and send it to ROS2 so it can be seen in ros2 topic list. In separate windows:

```bash
noetic
roscore 
```

```bash
noetic
rosbag play Downloads/recorded_data_FT.bag 
```

```bash
noetic
foxy
ros2 run ros1_bridge dynamic_bridge --bridge-all-topics
```

```bash
foxy
ros2 topic list
```

# ROS2 Subscriber/Publisher Node (Python)
Create a new package (can be called force_feedback)

```bash
foxy
cd ros2_ws/src/
ros2 pkg create force_feedback --build-type ament_python
```

Create a new Python node

```bash
foxy
cd ros2_ws/src/force_feedback/force_feedback/
touch force_reader.py
chmod +x force_reader.py
```
Now edit the below files which are added to the repository
force_reader.py
package.xml
setup.py

After the edits source the workspace
```bash
foxy
cd ros2_ws/
colcon build
source install/setup.bash
```
You can run the module by below. It will subscribe to /moca_red/ATI45_ft_handler/wrench and publish to the topics of /z_force and /joy/set_feedback

```bash
cd ~/ros2_ws/
ros2 run force_feedback haptic
```
# Haptic Feedback
First setup the necessary packages for the controller. More details are from:

[joy pkg](https://index.ros.org/p/joy/)

[Joy Feedback](https://docs.ros.org/en/api/sensor_msgs/html/msg/JoyFeedback.html)

```bash
foxy
cd ros2_ws
sudo apt install ros-foxy-joy
```
Always source
```bash
colcon build
source install/setup.bash
```
Run the joy

```bash
ros2 run joy joy_node
```
Now you can get position data by 
```bash
ros2 topic echo /joy
```

Now you can echo haptic feedback with (or for the force value, echo /z_force)
```bash
ros2 topic echo /joy/set_feedback
```

You can manually give vibration by: choosing intensity between 0.0-and 1.0)
```bash
ros2 topic pub /joy/set_feedback sensor_msgs/msg/JoyFeedback "type: 1 
id: 0
intensity: 0.5"
```
There you go!


