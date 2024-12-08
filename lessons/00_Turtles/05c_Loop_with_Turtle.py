
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.

"""



"""
if i want to write in a program some random stuff abnd not have it execute,
i put it in a comment block started by the three quotes
"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(width=600, height=600)     # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast.

# if i wanna do one line, i do a hashtag

tina.forward(50)
tina.left(25)
tina.forward(50)
tina.left(25)
tina.forward(50)
tina.left(25)
tina.forward(50)
tina.left(25)
tina.forward(50)
tina.left(25)
tina.forward(50)
tina.left(25)
tina.forward(50)
tina.left(25)
tina.forward(50)
tina.left(25)
tina.forward(50)
tina.left(25)
tina.forward(50)
tina.left(25)
tina.forward(50)
tina.left(25)
tina.forward(50)
tina.left(25)
tina.forward(50)
tina.left(25)
tina.forward(50)
tina.left(25)



for x in range(100):
    tina.forward(100)
    tina.left(36)



for x in range(40):
    tina.forward(50)
    tina.left(39)



turtle.exitonclick()                    # Close the window when we click on it





