import turtle
import time 

def square(side):
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)

square(20)
square(30)
square(40)
square(50)
time.sleep(5)