import turtle
from turtle import *

screen = turtle.Screen()
# Defining a turtle Instance
t = turtle.Turtle()
speed(10)

t.color("Black")
t.pensize(0.25)
t.penup()
t.goto(-200,125)
t.pendown()
t.forward(400)
t.right(90)
t.forward(266)
t.right(90)
t.forward(400)

#circle
t.penup()
t.goto(-80,-8)
t.pendown()
t.color('#DC143C')
t.left(90)
t.begin_fill()
t.circle(80)
t.end_fill()

t.color("Brown")
t.pensize(10)
t.penup()
t.goto(-200,125)
t.pendown()
t.forward(600)

turtle.done()