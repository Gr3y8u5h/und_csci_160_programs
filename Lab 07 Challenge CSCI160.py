import turtle

"""Joshua W George - joshua.w.george@ndus.edu - CSCI-160 Online - Lab 7 Challenge"""

'''Write a function named drawName (x, y) , which writes all the letters to the screen, evenly
spaced out. This will require a loop to access each letter in your name, as well as a variable to
determine the x , y location for each letter. You could even write drawHName(x, y) and
drawVName (x, y) , which would write out your letters either horizontally or vertically, again
evenly spaced, using x and y as a starting location for the first letter.'''

firstTurt = turtle.Turtle()  # Global initialization of turtle
name = 'JOSH'  # The name to be written


def drawJ(x, y):
    """Goto, draw, and fill the J.  X and Y parameters are for starting positions."""

    # Goto J

    firstTurt.begin_fill()
    firstTurt.fillcolor('black')
    firstTurt.penup()
    firstTurt.goto(x, y)
    firstTurt.setheading(270)
    firstTurt.pendown()

    # Draw the J

    firstTurt.forward(50)
    firstTurt.left(90)
    firstTurt.forward(50)
    firstTurt.right(90)
    firstTurt.forward(100)
    firstTurt.right(90)
    firstTurt.forward(50)
    firstTurt.right(90)
    firstTurt.forward(50)
    firstTurt.left(90)
    firstTurt.forward(50)
    firstTurt.left(90)
    firstTurt.forward(100)
    firstTurt.left(90)
    firstTurt.forward(150)
    firstTurt.left(90)
    firstTurt.forward(150)
    firstTurt.right(90)
    firstTurt.forward(50)
    firstTurt.left(90)
    firstTurt.forward(50)
    firstTurt.left(90)
    firstTurt.forward(150)

    firstTurt.end_fill()


def drawO(x, y):
    """Goto, draw, and fill the O.  X and Y parameters are for starting positions."""

    # Goto 0

    firstTurt.begin_fill()
    firstTurt.fillcolor('black')
    firstTurt.penup()
    firstTurt.goto(x, y)
    firstTurt.setheading(270)
    firstTurt.pendown()

    # Draw the O

    firstTurt.forward(200)
    firstTurt.left(90)
    firstTurt.forward(200)
    firstTurt.left(90)
    firstTurt.forward(200)
    firstTurt.left(90)
    firstTurt.forward(200)
    firstTurt.penup()

    firstTurt.end_fill()

    firstTurt.goto(x + 50, y - 50)
    firstTurt.setheading(270)
    firstTurt.begin_fill()
    firstTurt.fillcolor('medium spring green')
    firstTurt.pendown()
    firstTurt.forward(100)
    firstTurt.left(90)
    firstTurt.forward(100)
    firstTurt.left(90)
    firstTurt.forward(100)
    firstTurt.left(90)
    firstTurt.forward(100)
    firstTurt.penup()


    firstTurt.end_fill()


def drawS(x, y):
    """Goto, draw, and fill the S.  X and Y parameters are for starting positions."""

    # Goto S

    firstTurt.begin_fill()
    firstTurt.fillcolor('black')
    firstTurt.penup()
    firstTurt.goto(x, y)
    firstTurt.setheading(270)
    firstTurt.pendown()

    # Draw the S

    firstTurt.forward(125)
    firstTurt.left(90)
    firstTurt.forward(150)
    firstTurt.right(90)
    firstTurt.forward(25)
    firstTurt.right(90)
    firstTurt.forward(150)
    firstTurt.left(90)
    firstTurt.forward(50)
    firstTurt.left(90)
    firstTurt.forward(200)
    firstTurt.left(90)
    firstTurt.forward(125)
    firstTurt.left(90)
    firstTurt.forward(150)
    firstTurt.right(90)
    firstTurt.forward(25)
    firstTurt.right(90)
    firstTurt.forward(150)
    firstTurt.left(90)
    firstTurt.forward(50)
    firstTurt.left(90)
    firstTurt.forward(200)

    firstTurt.end_fill()


def drawH(x, y):
    """Goto, draw, and fill the H.  X and Y parameters are for starting positions."""

    # Goto H

    firstTurt.begin_fill()
    firstTurt.fillcolor('black')
    firstTurt.penup()
    firstTurt.goto(x, y)
    firstTurt.setheading(270)
    firstTurt.pendown()

    # Draw the H

    firstTurt.forward(200)
    firstTurt.left(90)
    firstTurt.forward(50)
    firstTurt.left(90)
    firstTurt.forward(75)
    firstTurt.right(90)
    firstTurt.forward(100)
    firstTurt.right(90)
    firstTurt.forward(75)
    firstTurt.left(90)
    firstTurt.forward(50)
    firstTurt.left(90)
    firstTurt.forward(200)
    firstTurt.left(90)
    firstTurt.forward(50)
    firstTurt.left(90)
    firstTurt.forward(75)
    firstTurt.right(90)
    firstTurt.forward(100)
    firstTurt.right(90)
    firstTurt.forward(75)
    firstTurt.left(90)
    firstTurt.forward(50)

    firstTurt.end_fill()


def drawHName(x, y):
    """Draws the name horizontally.  Uses parameters x and y to set first position of first letter."""

    for index in name:
        if index == 'J':
            drawJ(x, y)
        if index == 'O':
            drawO(x + 200, y)
        if index == 'S':
            drawS(x + 450, y)
        if index == 'H':
            drawH(x + 700, y)


def drawVName(x, y):
    """Draws the name vertically.  Uses parameters x and y to set first position of first letter."""

    for index in name:
        if index == 'J':
            drawJ(x, y)
        if index == 'O':
            drawO(x - 50, y - 225)
        if index == 'S':
            drawS(x - 50, y - 450)
        if index == 'H':
            drawH(x - 50, y - 675)


def main():
    """States the name to be written and asks for input to display Vertical or Horizontal.
    Sets the screen to maximum and sets the turtles parameters"""

    print()
    print('The name to be printed is "JOSH"')
    nameDirection = input('Enter H for horizontal, V for Vertical: ')

    scrn = turtle.Screen()
    scrn.setup(0, 0)
    scrn.bgcolor("medium spring green")

    firstTurt.shape('circle')
    firstTurt.color('red')
    firstTurt.shapesize(1, 1, 1)
    firstTurt.pensize(1)
    firstTurt.pencolor('red')
    firstTurt.speed(5)

    # Chooses which way to draw.
    if nameDirection == 'H' or nameDirection == 'h':
        scrn.setup(1.0, 1.0)  # Full screen mode
        # sets the position of the first letter
        x = -425
        y = 100
        drawHName(x, y)
        scrn.exitonclick()
    elif nameDirection == 'V' or nameDirection == 'v':
        scrn.setup(1.0, 1.0)  # Full screen mode
        # sets the position of the first letter
        x = -50
        y = 475
        drawVName(x, y)
        scrn.exitonclick()
    exit()


main()
