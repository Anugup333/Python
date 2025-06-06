 #  Write a program to draw and fill circles with different colour

import turtle as t
import time 

c = ["blue","red","pink"]
for i in range(3):
    t.fillcolor(c[i])
    t.begin_fill()
    t.circle(70)
    t.end_fill()
    
time.sleep(5)