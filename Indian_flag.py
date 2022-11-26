import turtle
from turtle import *

# screen for output
screen = turtle.Screen()
# Defining a turtle Instance
t = turtle.Turtle()
speed(10)

# initially penup()
t.penup()
t.goto(-200, 125)
t.pendown()
# Orange Rectangle
#white rectangle
t.color("orange")
t.begin_fill()
t.forward(400)
t.right(90)
t.forward(84)
t.right(90)
t.forward(400)
t.end_fill()
t.left(90)
t.forward(84)

t.color("green")
t.begin_fill()
t.left(90)
t.forward(400)
t.right(90)
t.forward(84)
t.right(90)
t.forward(400)
t.right(90)
t.forward(84)
t.end_fill()
t.penup()

t.goto(35,0)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(36)
t.end_fill()

# Big White Circle
t.penup()
t.goto(30, 0)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(30)
t.end_fill()

t.penup()
t.goto(-27, -4)
t.pendown()
t.color("navy")
for i in range(24):
    t.begin_fill()
    t.circle(2)
    t.end_fill()
    t.penup()
    t.forward(7)
    t.right(15)
    t.pendown()
    
# Small Blue Circle
t.color("navy")
t.penup()
t.goto(10, 0)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

#The spokes of the Indian Flag
t.penup()
t.goto(0, 0)
t.pendown()
t.pensize(1)
for i in range(24):
    t.forward(30)
    t.backward(30)
    t.left(15)
    
t.color("Brown")
t.pensize(10)
t.penup()
t.goto(-200,125)
t.right(180)
t.pendown()
t.forward(800)                    

t.done()
