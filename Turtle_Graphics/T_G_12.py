import turtle as t
import time 

def Draw_bar_Chart(t,height):
    t.begin_fill()  # Start filling this shape
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

Mozilla_Firefox = 45
Chrome = 30
IE = 15
Others = 10
S =  [Mozilla_Firefox, Chrome, IE, Others]
maxheight = max(S)
num_of_bars = len(S)
border = 10
w = t.Screen()
w.setworldcoordinates(0,0,40 * num_of_bars + border, maxheight + border)
w.bgcolor("pink")
# t.bgcolor("pink")
t.color("#000000")
t.fillcolor("#DB148E")
t.pensize(3)
for a in S:
    Draw_bar_Chart(t,a)

    


time.sleep(5)