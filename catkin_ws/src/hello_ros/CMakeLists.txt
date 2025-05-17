# sudo apt update
# sudo apt install git
# git clone https://github.com/freshmea/kuLimo.git


cmake_minimum_required(VERSION 3.0.2)
project(hello_ros)
find_package(catkin REQUIRED COMPONENTS
  dynamic_reconfigure
  geometry_msgs
  roscpp
  rospy
  std_msgs
  message_generation
)

catkin_python_setup()

generate_dynamic_reconfigure_options(
  cfg/SimpleParameter.cfg
  cfg/Turtle.cfg
)

add_message_files(
  FILES
  MyTopic.msg
)

generate_messages()


catkin_package()

catkin_install_python(PROGRAMS
  scripts/hello
  scripts/moveTurtle
  scripts/moveTurtleClass
  scripts/mtpub
  scripts/mtsub
  scripts/mpub
  scripts/msub
  scripts/msub2
  scripts/simpleServiceServer
  scripts/simpleServiceClient
  scripts/simpleServiceClient2
  scripts/simpleParameter
  scripts/simpleParameter2
  scripts/myTopicPub
  scripts/myTopicSub
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY
  launch
  param
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
