# widowx_arm_dev

Pre-release ROS support for WidowX including MoveIt! and Pick & Place demo. Not intended for use by humans.

Using SR300 for pointcloud.

Depending on interbotix/arbotix_ros/turtlebot2i [branch](https://github.com/Interbotix/arbotix_ros/tree/turtlebot2i) for gripper controller.

roslaunch widowx_arm_bringup arm_moveit.launch sim:=false sr300:=true

roslaunch widowx_block_manipulation block_sorting_demo.launch
