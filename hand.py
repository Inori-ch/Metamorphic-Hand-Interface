##
# File: hand.py
# Author: Inori Chan (12332378@mail.sustech.edu.cn)
# Brief:
# Date: 2023-09-26
# Copyright: Copyright (c) 2023
#
##
from scripts import action

def Grab():
  grab = action.Action("configs\\grab.yaml")
  grab.Run()

def Release():
  release = action.Action("configs\\release.yaml")
  release.Run()