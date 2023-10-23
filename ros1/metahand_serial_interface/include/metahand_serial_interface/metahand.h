/**
 * @file metahand.h
 * @author 陈祈 (inorichen77@gmail.com)
 * @brief
 * @version 0.1
 * @date 2023-10-23
 *
 * @copyright Copyright (c) 2023
 *
 */

#ifndef __METAHAND_H__
#define __METAHAND_H__

#include <ros/ros.h>

#include <string>
#include <unordered_map>

#include "metahand_msgs/hand_control_signal.h"

class MetaHand {
  /**
   * @brief
   *
   */
 private:
  ros::NodeHandle nh_;
  ros::ServiceServer handSrv_;
  std::string serialPort_;
  int baudRate_;
  int timeOut_;

  std::unordered_map<std::string, std::string> gesture_;

 public:
  /**
   * @brief Construct a new Meta Hand object
   *
   * @param nh
   */
  explicit MetaHand(const ros::NodeHandle &nh);
  /**
   * @brief Destroy the Meta Hand object
   *
   */
  ~MetaHand();
  /**
   * @brief
   *
   * @return int
   */
  int MainLoop();
  /**
   * @brief
   *
   * @param command
   * @param result
   * @return true
   * @return false
   */
  bool HandServer(metahand_msgs::hand_control_signal::Request &command,
                  metahand_msgs::hand_control_signal::Response &result);
};

#endif  // __METAHAND_H__