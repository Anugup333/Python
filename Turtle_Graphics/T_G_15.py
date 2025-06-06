import turtle
import time 
s = turtle.getscreen()
turtle.ht()
t1 = turtle.Turtle()
# t1.circle(100)
# t1.fillcolor("green")
# t1.begin_fill()
# t1.circle(50)
# t1.end_fill()

t1.fillcolor("lightgreen")
t1.begin_fill()
t1.penup()
t1.goto(100,100)
t1.pendown()
t1.goto(-100,100)
t1.goto(-100,-100)
t1.goto(100,-100)
t1.goto(100,100)
t1.end_fill()

time.sleep(5)