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
      data = self.serialPort_.read_all()
      result = data.decode('ascii')
      if result == '':
        # print('none')
        continue
      else:
        # result = chardet.detect(data)
        # print(result)
        break
      sleep(0.02)
    return result
  
  def Send(self, data):
    """Send data to serial port

    Args:
        data (bytes): command
    """
    if (self.serialPort_.isOpen()):
      self.serialPort_.write((data + '\r\n').encode('ascii'))  # 编码
      sleep(0.02)
      # print("success ", data)
    # else:
      # print("failed!!!")
  
  