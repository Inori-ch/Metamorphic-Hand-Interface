##
# File: IO.py
# Author: Inori Chan (12332378@mail.sustech.edu.cn)
# Brief:
# Date: 2023-09-27
# Copyright: Copyright (c) 2023
#
##
import serial
from utils import serial_port_init
from time import sleep
import chardet

class Interface:
  def __init__(self) -> None:
    self.serialPort_ = serial_port_init.Init()

  def Read(self):
    """Read data from serial port

    Returns:
        data: bytes recieved
    """
    while True:
      data = self.serialPort_.readall()
      if data == "":
        print('none')
        continue
      else:
        result = chardet.detect(data)
        print(result)
        break
      sleep(0.02)
    return data
  
  def Send(self, data):
    """Send data to serial port

    Args:
        data (bytes): command
    """
    if (self.serialPort_.isOpen()):
      self.serialPort_.write(data.encode('utf-8'))  # 编码
      # print("success ", data)
    # else:
      # print("failed!!!")
  
  