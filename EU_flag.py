import turtle
from turtle import *

s = turtle.Screen()
t = turtle.Turtle()
t.speed(10)

t.penup()
t.goto(-210,210)
t.pendown()

t.color("#003399")
t.begin_fill()
t.forward(400)
t.right(90)
t.forward(266)
t.right(90)
t.forward(400)
t.right(90)
t.end_fill()

t.penup()
t.goto(-107,90)
t.pendown()
t.color("white")

i=0
while i<1:
	k=0
	while k<12:
		t.begin_fill()
		j=0
		while j<5:
	   		t.forward(14)
	   		t.right(144)
	   		j=j+1
	  
		t.end_fill()  
		t.penup()
		t.right(30)
		t.forward(46)
		t.pendown()
		k=k+1
	i=i+1				

t.penup()
t.goto(-210,210)
t.pendown()
t.color("brown")
t.pensize(10)
t.right(180)
t.forward(600)

turtle.done()
