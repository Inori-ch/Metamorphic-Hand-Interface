##
# File: action.py
# Author: Inori Chan (12332378@mail.sustech.edu.cn)
# Brief:
# Date: 2023-09-27
# Copyright: Copyright (c) 2023
#
##

from utils import *
from scripts import IO
from time import sleep

class Action:
  """Action base, instance with diff config path to grab or release
  """
  def __init__(self, commandPath) -> None:
    self.commandPath_ = commandPath

  def Run(self):
    sleep(0.2)
    interface = IO.Interface()
    command = load_config.Load(self.commandPath_)
    interface.Send(command['command'])
    sleep(1)
    while(True):
      callBack = interface.Read()
      print(callBack)
      if(callBack == 'Arrive'):
        break
      sleep(0.2)

