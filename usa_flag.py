import turtle
from turtle import *

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(10)

t.penup()
t.goto(-210,210)
t.pendown()
t.color("red")
i=1
while i<8:
	t.begin_fill()
	t.forward(400)
	t.right(90)
	t.forward(16)
	t.right(90)
	t.forward(400)
	t.right(90)
	t.forward(16)
	t.end_fill()
	t.backward(32)
	t.right(90)
	i=i+1
	
t.penup()
t.goto(-210,210)
t.pendown()

t.color("blue")
t.begin_fill()
t.forward(160)
t.right(90)
t.forward(113)
t.right(90)
t.forward(160)
t.right(90)
t.forward(113)
t.end_fill()
t.right(90)

t.penup()
t.goto(-198,200)
t.pendown()

t.color("white")

m=0
while m<5:
	k=0
	while k<6:
		t.begin_fill()
		j=0
		while j<5:
	   		t.forward(12)
	   		t.right(144)
	   		j=j+1
	  
		t.end_fill()  
		t.penup()
		t.forward(26)
		t.pendown()
		k=k+1
	t.penup()
	t.backward(156)
	t.right(90)
	t.forward(23)
	t.left(90)
	m=m+1
	
t.penup()
t.goto(-185,187)
t.pendown()

t.color("white")

m=0
while m<4:
	k=0
	while k<5:
		t.begin_fill()
		j=0
		while j<5:
	   		t.forward(12)
	   		t.right(144)
	   		j=j+1
	  
		t.end_fill()  
		t.penup()
		t.forward(26)
		t.pendown()
		k=k+1
		
	t.penup()
	t.backward(130)
	t.right(90)
	t.forward(23)
	t.left(90)
	m=m+1	

t.penup()
t.goto(-210,210)
t.pendown()
t.color("brown")
t.pensize(10)
t.right(90)
t.forward(600)

turtle.done()

								
