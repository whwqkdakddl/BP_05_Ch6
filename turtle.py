import turtle
 
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.lt(90)
 
for i in range (6):
    t.fd(100); t.fd(-30); t.lt(60); t.fd(30); t.fd(-30)
    t.rt(120); t.fd(30); t.fd(-30); t.lt(60); t.fd(-70); t.lt(60
import turtle
t = turtle.Turtle()
t.color("red")
 
for i in range(10):
    for j in range(1,6):
        t.lt(144)
       t.fd(200)
    t.lt(10)
import random as rd
import turtle
 
t = turtle.Turtle()
t.shape("turtle")
 
for i in range(10):
    x=rd.randint(-150,150)
    y=rd.randint(-150,150)
    r=rd.randint(1,100)
 
    t.up()
    t.goto(x,y)
    t.down()
    t.circle(r)
import turtle
 
t = turtle.Turtle()
t.shape("turtle")
 
for i in range(5):
    t.fd(200)
    t.rt(90)
    t.fd(20)
    t.rt(90)
    t.fd(200)
    t.lt(90)
    t.fd(20)
    t.lt(90)
 mport turtle
 
t = turtle.Turtle()
t.shape("turtle")
t.color("red", "yellow")
t.begin_fill()
while True:
    t.forward(200)
    t.left(170)
    if abs(t.pos())< 1:
        break
t.end_fill()
 import turtle
import math

t = turtle.Turtle()
t.shape("turtle")

for i in range(360):
    sine = math.sin(math.pi * i / 180.0)
    print(sine)
    t.goto(i, sine * 100)                                                             
                                                              
