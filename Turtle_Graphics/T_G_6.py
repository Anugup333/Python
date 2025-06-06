# write a program to draw a square with filled colour

import turtle
import time 
turtle.fillcolor("purple")
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

time.sleep(5)