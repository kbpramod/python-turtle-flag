import turtle
from turtle import *

screen = turtle.Screen()
# Defining a turtle Instance
t = turtle.Turtle()
speed(20)

# initially penup()
t.penup()
t.goto(-200, 125)
t.pendown()

#colors
colors = ['white','blue','red']

for i in range(0,3):
	t.color(colors[i])
	t.begin_fill()
	t.forward(400)
	t.right(90)
	t.forward(89)
	t.right(90)
	t.forward(400)
	t.end_fill()
	t.right(180)

t.color("Brown")
t.pensize(10)
t.penup()
t.goto(-200,125)
t.right(90)
t.pendown()
t.forward(600)

t.color("Black")
t.pensize(0.5)
t.penup()
t.goto(-200,125)
t.pendown()
t.left(90)
t.forward(400)
t.right(90)
t.forward(267)
t.right(90)
t.forward(400)

t.penup()
t.goto(200, -1250)
t.pendown()

turtle.done()
