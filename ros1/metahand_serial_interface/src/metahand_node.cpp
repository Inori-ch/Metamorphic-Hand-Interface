/**
 * @file metahand_node.cpp
 * @author 陈祈 (inorichen77@gmail.com)
 * @brief
 * @version 0.1
 * @date 2023-10-23
 *
 * @copyright Copyright (c) 2023
 *
 */
#include "metahand.h"

int main(int argc, char **argv) {
  ros::init(argc, argv, "metahand");
  ros::NodeHandle nh("~");
  MetaHand hand(nh);
  return 0;
}