##
# File: hand.py
# Author: Inori Chan (12332378@mail.sustech.edu.cn)
# Brief:
# Date: 2023-09-26
# Copyright: Copyright (c) 2023
#
##
import hand
from time import sleep

if __name__ == "__main__":
  hand_ = hand.Hand()
  hand_.Run('idle')

  hand_.Run('open')
  