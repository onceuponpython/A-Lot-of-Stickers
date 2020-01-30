# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 20:07:20 2019

@author: Owner
"""
import turtle
t=turtle.Turtle()

t.pendown()
t.color("green")
t.width(2)

#first 1/2 of tree
t.forward(200)
t.left(135)
t.forward(200)
t.right(135)
t.forward(100)
t.left(135)
t.forward(150)
t.right(135)
t.forward(60)
t.left(135)
t.forward(100)
t.left(90)

#Second 1/2 of tree (reverse)
t.forward(100)
t.left(135)
t.forward(60)
t.right(135)
t.forward(150)
t.left(135)
t.forward(100)
t.right(135)
t.forward(200)
t.left(135)
t.forward(200)

#trunk
t.penup()
t.backward(75)
t.pendown()
t.color("brown")
t.width(4)
t.right(90)
t.forward(100)
t.left(90)
t.forward(75)
t.right(90)
t.backward(100)

#mirror image
t.penup()
t.forward(800)
t.color("blue")
t.width(2)
t.pendown()

#trunk
t.penup()
t.backward(75)
t.pendown()
t.color("brown")
t.width(4)

t.right(90)
t.backward(100)
t.left(90)
t.backward(75)
t.right(90)
t.forward(100)


t.right(90)
t.forward(200)
t.left(-135)
t.forward(200)
t.right(-135)
t.forward(100)
t.left(-135)
t.forward(150)
t.right(-135)
t.forward(60)
t.left(-135)
t.forward(100)
t.left(-90)

#Second 1/2 of tree (reverse)
t.forward(100)
t.left(-135)
t.forward(60)
t.right(-135)
t.forward(150)
t.left(-135)
t.forward(150)
t.right(-135)
t.forward(100)
t.left(-135)
t.forward(200)
#t.right(90)