import turtle
from turtle import *

screen = turtle.Screen()

t = turtle.Turtle()
t.speed(10)

t.penup()
t.goto(-220,150)
t.pendown()

t.color('Black')
t.forward(440)
t.right(90)
t.forward(320)
t.right(90)
t.forward(440)

t.penup()
t.goto(-220,120)
t.pendown()

t.color('blue')
t.begin_fill()
t.left(180)
t.forward(440)
t.right(90)
t.forward(50)
t.right(90)
t.forward(440)
t.end_fill()

t.penup()
t.goto(-220,-90)
t.pendown()

t.color('blue')
t.begin_fill()
t.left(180)
t.forward(440)
t.right(90)
t.forward(50)
t.right(90)
t.forward(440)
t.end_fill()

t.penup()
t.goto(-60,-40)
t.pendown()

t.color('blue')

t.pensize(11)
t.right(180)
t.forward(109)
t.left(120)
t.forward(109)
t.left(120)
t.forward(109)


t.penup()
t.goto(-60,28)
t.pendown()

t.right(120)
t.color('blue')
t.pensize(11)
t.right(180)
t.forward(109)
t.left(120)
t.forward(109)
t.left(120)
t.forward(109)

t.penup()
t.goto(-220,150)
t.pendown()
t.color('brown')
t.left(90)
t.forward(600)

turtle.done()