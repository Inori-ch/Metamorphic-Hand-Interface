##
# File: action.py
# Author: Inori Chan (12332378@mail.sustech.edu.cn)
# Brief:
# Date: 2023-09-27
# Copyright: Copyright (c) 2023
#
##

from utils import *
from time import sleep

class Action:
  """Action base, instance with diff config path to grab or release
  """
  def __init__(self, command) -> None:
    self.command_ = command

  def Run(self, interface):
    sleep(0.2)
    interface.Send(self.command_)
    sleep(1)
    # while(True):
    #   sleep(0.2)
    # callBack = interface.Read()
    # print(callBack)
      # if(callBack == ''):
      #   break

