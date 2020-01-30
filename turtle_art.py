# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 07:47:13 2019

@author: Owner
"""

import turtle 
import random


t=turtle.Turtle()
#speed choices "slowest", "slow", "normal", "fast" & "fastest"
t.speed("fastest")
#t.color("blue")
t.width(2)


num_sides=3
turn_amount=360/num_sides
repeats=5

color_list=["blue", "pink", "yellow", "orange", "green", "orchid", "deep pink", "darkseagreen", "darkmagenta"]

#the range gives you the number of shapes that will be created
for z in range(25):
  dist=(random.randrange(10,45))
  x_coord=(random.randrange(-150, 150))
  y_coord=(random.randrange(-150, 150))
  t.color(random.choice(color_list))
  t.penup()
  t.goto(x_coord, y_coord)
  
  t.pendown()
  #repeats gives you the number of inner shapes
  for y in range (repeats):
    #draw inner shape
    for i in range (num_sides):
      t.forward(dist)
      t.right(turn_amount)
        
    t.right(360/repeats)
  t.pendown()
    
t.hideturtle
        