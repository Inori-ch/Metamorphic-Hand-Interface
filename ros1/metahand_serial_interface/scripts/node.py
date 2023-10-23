#! /home/inori/anaconda3/envs/metahand/bin/python

##
# File: node.py
# Author: Inori Chan (12332378@mail.sustech.edu.cn)
# Brief:
# Date: 2023-10-22
# Copyright: Copyright (c) 2023
#
##
import rospy
import sys
import hand

def main(args):
  """_summary_

  Args:
      args (_type_): _description_
  """
  metahand_ = hand.Hand()
    
  

if __name__ == '__main__':
  main(sys.argv)
  