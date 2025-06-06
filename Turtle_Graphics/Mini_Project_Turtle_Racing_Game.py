"""Algorithm
   STEP 1: Design the Track
   STEP 2: Place all the turtles at the appropriate position to start the race 
   STEP 3: Use the for loop to run over the track and a random number to move 
           the turtle forward by x pixels
   STEP 4: END 
    """


from turtle import*
from random import*

title('tirtle F1 Racing Game ')

''' Step 1 : Design the track '''

speed(10)
penup()
goto(-240,240)  # Initial position of the Track
z = 0
y = 25

for x in range(6):   # iterate to draw six lines 
    write(x)     # Mark distance at the top of lines 
    right(90)    # Change direction facing downwards
    forward(10)  # Move 10 steps ahead
    pendown()     # Open pen to draw 
    forward(150)  # move 150 steps ahead
    penup()      # Close the pen
    backward(160)  # move 160 steps backward
    left(90)       # change direction toward left
    forward(y)     # Move y step Forward

''' STEP 2: Write the code the three turtles and place them at 
    the proper position before the start of the first line '''

t1 = Turtle()         # First turtle - Red Coloured
t1.penup()
t1.goto(-260,200)
t1.color("red")
t1.shape("turtle")


t2 = Turtle()         # Second turtle - Black Coloured
t2.penup()
t2.goto(-260,150)
t2.color("black")
t2.shape("turtle")


t3 = Turtle()         # third turtle - Green Coloured
t3.penup()
t3.goto(-260,100)
t3.color("green")
t3.shape("turtle")

'''STEP 3: Moving the turtle Randomly'''

for i in range(50):
    t1.forward(randint(1,5))
    t2.forward(randint(1,5))
    t3.forward(randint(1,5))