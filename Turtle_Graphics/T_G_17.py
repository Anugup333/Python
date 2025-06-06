import turtle
import time 
t1 = turtle.Turtle()

t1.pencolor("blue")
t1.fillcolor("yellow")
t1.shape("square")
t1.shapesize(5,5,5)
t1.penup()
t1.goto(200,200)



t1.stamp()   # Copy of turtle
t1.goto(-200,200)   # change Direction of turtle
t1.stamp()
t1.goto(-200,-200)
t1.stamp()
t1.goto(200,-200)

time.sleep(5)