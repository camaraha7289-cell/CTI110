# Anthony Camara-Hernandez
# 4/29/2026
# P4 Lab1
# Use trurtle and loops to draw a square and a triangle
#

import turtle             # Allows us to use turtles

# Create the turtle window and drawing object
win = turtle.Screen()
turtle.bgcolor("skyblue")
pen = turtle.Turtle()


# Set turtle options 
pen.pensize(5)
pen.pencolor("brown")
pen.shape ("arrow")


# Starting position.
pen.penup()
pen.goto(-75,-75)
pen.pendown()
# Code to draw the shapes 
for side in range(4) :
    pen.forward(150)
    pen.left(90)

# Move to top-left corner of square
pen.penup()
pen.goto(-75, 75)
pen.setheading(0)   # Face right
pen.pendown()



# While loop that executes 3 time
sides = 0 

while sides < 3: 
    pen.forward(150)
    pen.left(120)
    sides = sides - 1 





# Wait for user to close window
win.mainloop()
