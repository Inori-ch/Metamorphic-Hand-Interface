##
# File: serial_port_init.py
# Author: Inori Chan (12332378@mail.sustech.edu.cn)
# Brief:
# Date: 2023-09-26
# Copyright: Copyright (c) 2023
#
##
from utils.load_config import Load
import serial
import sys

def Init():
  """Init serial port according to parameters in configs/serial.yaml

  Returns:
      serialPort (serial.Serial): object
  """
  param = Load("configs/serial.yaml")
  try:
    serialPort = serial.Serial(port = param['port'], baudrate = param['baud_rate'], timeout = param['time_out'])
    print('Open serial port', param['port'], 'success!!!')
    print('Baudrate:', param['baud_rate'], 'timeout:', param['time_out'])
    return serialPort
  except:
    print("Serial initialize failed!!")
    sys.exit( 1)
  
