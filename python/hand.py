##
# File: hand.py
# Author: Inori Chan (12332378@mail.sustech.edu.cn)
# Brief:
# Date: 2023-09-26
# Copyright: Copyright (c) 2023
#
##
from scripts import *
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
    self.interface_ = IO.Interface()
    self.gesture_ = load_config.Load('configs/gesture.yaml')
    sleep(1)
    self.Run('idle')
  
  def Run(self, command):
    """Move the hand

    Args:
        command (string): eg. 'grab', 'ojbk', 'open'
    """
    self.action_ = action.Action(self.gesture_[command])
    self.action_.Run(self.interface_)
