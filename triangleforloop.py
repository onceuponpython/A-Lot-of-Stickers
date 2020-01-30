# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 20:04:19 2020

@author: Owner
"""

import turtle
t=turtle.Turtle()
t.shape("turtle")

#for loop
for i in range(3):
  
  #if-else statement
  if i==0:
    t.pencolor("red")
  else:
    t.pencolor("green")
  t.forward(70)
  t.right(120)
