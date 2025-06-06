# Undone Turtle Actions
import turtle
import time 
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t1.penup()
t2.penup()
t1.pencolor("blue")
t2.pencolor("red")

t1.goto(-200,0)
t2.goto(200,0)
t2.left(180)
t1.pendown()
t2.pendown()

for i in range(1,11):
    t2.forward(35)
    t2.penup()
    t2.forward(5)
    t2.pendown()

for e in range(3):
    for i in range(1,11):
        t2.undo()
        t2.undo()
        t2.undo()
        t2.undo()
        t1.forward(35)
        t1.penup()
        t1.forward(5)
        t1.pendown()
    for i in range(1,11):
        t1.undo()
        t1.undo()
        t1.undo()
        t1.undo()
        t2.forward(35)
        t2.penup()
        t2.forward(5)
        t2.pendown()
        


time.sleep(5)