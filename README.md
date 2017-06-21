# widowx_arm_dev

Pre-release ROS support for WidowX including MoveIt! and Pick & Place / Sorting demo. Not intended for use by humans.

Using SR300 for pointcloud.

Depending on interbotix/arbotix_ros/turtlebot2i [branch](https://github.com/Interbotix/arbotix_ros/tree/turtlebot2i) for gripper controller.

## Quick Start:

mkdir -p ~/widowx_arm/src

cd ~/widowx_arm/src

git clone https://github.com/r3n33/widowx_arm_dev.git .

git clone https://github.com/Interbotix/arbotix_ros.git -b turtlebot2i

cd ~/widowx_arm

catkin_make

roslaunch widowx_arm_bringup arm_moveit.launch sim:=false sr300:=false

## Object manipluation 

roslaunch widowx_arm_bringup arm_moveit.launch sim:=false sr300:=true

roslaunch widowx_block_manipulation block_sorting_demo.launch
