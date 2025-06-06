#  Write a program to display the polygon using Python's turtle module

import turtle
import time

def polygon(side):
    for i in range(8):
        turtle.forward(side)
        turtle.left(45)

polygon(50)

#  Same as that 

# turtle.forward(50)
# turtle.left(45)
# turtle.forward(50)
# turtle.left(45)
# turtle.forward(50)
# turtle.left(45)
# turtle.forward(50)
# turtle.left(45)
# turtle.forward(50)
# turtle.left(45)
# turtle.forward(50)
# turtle.left(45)
# turtle.forward(50)
# turtle.left(45)
# turtle.forward(50)

time.sleep(5)