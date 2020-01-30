# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 20:07:18 2020

@author: Owner
"""

import turtle
t=turtle.Turtle()
t.shape("turtle")

#outer loop
for i in range(8):
  t.right(45)
  
  #square with for loop
  for i in range(4):
    if i == 2:
      t.pencolor("blue")
    else:
      t.pencolor("hot pink")
    t.forward(50)
    t.right(90)
