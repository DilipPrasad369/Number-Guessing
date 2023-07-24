# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 16:56:45 2021

@author: HOME
"""

from random import randrange
n=randrange(1,11,1)
while True:
    v=int(input())
    if n==v:
        print("you win!")
        break
    else:
      print("smaller") if n<v else print("bigger")