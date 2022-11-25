import turtle
from turtle import *

s = turtle.Screen()
t = turtle.Turtle()
t.speed(10)

t.penup()
t.goto(-210,210)
t.pendown()

t.color("red")
t.begin_fill()
t.forward(400)
t.right(90)
t.forward(133)
t.right(90)
t.forward(400)
t.right(90)
t.end_fill()

t.right(90)
t.color("yellow")
t.begin_fill()
t.forward(400)
t.right(90)
t.forward(133)
t.right(90)
t.forward(400)
t.right(90)
t.end_fill()

t.penup()
t.goto(-210,210)
t.pendown()

t.right(180)
t.color("brown")
t.pensize(10)
t.forward(500)

turtle.done()
