import turtle
import time 
s = turtle.getscreen()
turtle.ht()
s.title("Moving turtle like a fan")
t1 = turtle.Turtle()
t1.pencolor("yellow")
t1.shape("turtle")
t1.shapesize(10,10,10)
for angle in range(0,901,90):
    t1.left(90)
time.sleep(5)