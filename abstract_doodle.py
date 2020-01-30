# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 10:16:25 2019

@author: Owner
"""

import turtle

t=turtle.Turtle()
#speed choices "slowest", "slow", "normal", "fast" & "fastest"
t.speed("slowest")
#t.color("blue")
t.width(2)
#t.pendown()

def triangle(side, angle):
    for i in range(3):
        t.forward(side)
        t.right(angle)
        
#triangle(100, 120)

def spiral_doodle(length, angle):
    for i in range(4):
        t.forward(length)
        t.right(angle)
        t.forward(length)
        t.right(angle)
        t.forward(length)
        t.right(angle)
        t.forward(length)
        t.right(angle)
        t.forward(length/4)
        t.right(angle)
        t.forward(length/4)
        
def spiral_doodle2(length, angle):
    for i in range(4):
        t.forward(length)
        t.right(angle)
        t.forward(length)
        t.right(angle)
        t.forward(length/2)
        t.right(angle)
        t.forward(length/2)
        t.right(angle)
        t.forward(length)
        t.right(angle)
        t.forward(length/4)
        t.right(angle)
        t.forward(length/4)
        t.right(angle)
        t.forward(length/2)
    
spiral_doodle(100, 90)  
spiral_doodle2(100, 90)
triangle(150, 100)

t.hideturtle