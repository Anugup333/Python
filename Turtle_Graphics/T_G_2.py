#  Write a program to draw the square using Python's Turtle Module
import turtle
import time

# same as that 

# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)

def square(side):
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)

square(200)
            
time.sleep(5)