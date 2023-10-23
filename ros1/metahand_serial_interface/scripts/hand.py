#! /home/inori/anaconda3/envs/metahand/bin/python

##
# File: hand.py
# Author: Inori Chan (12332378@mail.sustech.edu.cn)
# Brief:
# Date: 2023-09-26
# Copyright: Copyright (c) 2023
#
##
import rospy
from metahand_msgs.srv import *

from utils import *
from time import sleep

class Hand:
  """Provide metamorphic hand interface
     usage: 
     import hand
     hand_ = hand.Hand() # Initialize
     hand_.Run('idle') # gesture
  """
  def __init__(self):
    """Initialize serial interface & Load the commands from yaml
    """
    rospy.init_node('metahand', anonymous=True)
    self.serialServer_ = rospy.Service('metahand_serial_interface', hand_control_signal, self.callback)
    self.interface_ = IO.Interface()
    # self.gesture_ = load_config.Load('configs/gesture.yaml')
    self.gesture_ = rospy.get_param('/metahand_param/gesture')
    sleep(1)
    self.Run('idle')
    sleep(1)
    self.MainLoop()
  
  def callback(self, command):
    print(command.command.data)
    self.Run(command.command.data)
    sleep(10)
    return True
  
  def Run(self, command):
    """Move the hand

    Args:
        command (string): eg. 'grab', 'ojbk', 'open'
    """
    self.action_ = action.Action(self.gesture_[command])
    self.action_.Run(self.interface_)
    
  def MainLoop(self):
    while True:
      callBack = self.interface_.Read()
      sleep(0.2)
      if callBack == '':
        continue
      print(callBack)
