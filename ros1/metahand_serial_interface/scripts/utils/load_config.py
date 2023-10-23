#! /home/inori/anaconda3/envs/metahand/bin/python

##
# File: load_config.py
# Author: Inori Chan (12332378@mail.sustech.edu.cn)
# Brief:
# Date: 2023-09-27
# Copyright: Copyright (c) 2023
#
##
import yaml
import os

def Load(configPath):
  path = os.path.join(os.path.abspath("./Metamorphic-Hand-Interface"), configPath)
  file = open(path, 'r', encoding = "utf-8")
  data = file.read()
  file.close()
  param = yaml.load(stream = data, Loader = yaml.FullLoader)
  return param
