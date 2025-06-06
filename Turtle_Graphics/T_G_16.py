import turtle
import time 
t1 = turtle.Turtle()

t1.fillcolor("lightgreen")
t1.begin_fill()
t1.penup()
t1.goto(200,200)
t1.pendown()
t1.goto(-200,200)
t1.goto(-200,-200)
t1.goto(200,-200)
t1.goto(200,200)
t1.end_fill()

# draw small squares
txy = [(150,150,"navy"),(-25,150,"olive"),(-25,-25,"maroon"),(150,-25,"red")]
for xyc in txy:
    x,y,c = xyc
    t1.fillcolor(c)
    t1.begin_fill()
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    t1.goto(x-125,y)
    t1.goto(x-125,y-125)
    t1.goto(x,y-125)
    t1.goto(x,y)
    t1.end_fill()
time.sleep(5)
