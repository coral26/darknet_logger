cmake_minimum_required(VERSION 2.8.3)
project(darknet_logger)

find_package(catkin REQUIRED COMPONENTS
  rospy
  rosbag
  darknet_ros_msgs
)

catkin_python_setup()

catkin_package()

