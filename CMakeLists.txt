cmake_minimum_required(VERSION 2.8.3)
project(oliviaros)

find_package(catkin REQUIRED COMPONENTS
   roscpp
   rospy
   std_msgs
   message_generation
    message_runtime
  std_msgs
  std_srvs
  tf
  angles

)

catkin_python_setup()


add_message_files(
    FILES
    state.msg
    RAW_GPS.msg
)



add_service_files(
  FILES
  setarm.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
  INCLUDE_DIRS include
  LIBRARIES link
  CATKIN_DEPENDS roscpp std_msgs tf geometry_msgs
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)
