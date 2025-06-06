# 1- Fill circle with red colour 
# 2- Display the text message "Circle!" inside the Circle

import turtle
import time 
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(70)
turtle.end_fill()
turtle.penup()
turtle.goto(-25,50)
turtle.hideturtle()
turtle.write('Circle!', font=('Arial',20,"bold"))


time.sleep(5)