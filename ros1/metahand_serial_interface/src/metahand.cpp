/**
 * @file metahand.cpp
 * @author 陈祈 (inorichen77@gmail.com)
 * @brief
 * @version 0.1
 * @date 2023-10-23
 *
 * @copyright Copyright (c) 2023
 *
 */
#include "metahand.h"

MetaHand::MetaHand(const ros::NodeHandle &nh) : nh_(nh) {
  // ROS init
  // Param init
  // Serial port init

  // go idle

  // main loop
}

MetaHand::~MetaHand() {
  // close serial port
}

int MetaHand::MainLoop() {
  while (ros::ok()) {
    // read data from serial port
    ros::spinOnce();
  }
}

bool MetaHand::HandServer(
    etahand_msgs::hand_control_signal::Request &command,
    metahand_msgs::hand_control_signal::Response &result) {
  // send command to serial port
  return true;
}