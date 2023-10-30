import turtle

"""Joshua W George - joshua.w.george@ndus.edu - CSCI-160 Online - Lab 7 Part 2"""

'''
Assignment
Write a program using turtle graphics which writes your initials, or any other three unique letters,
to the display. Look to your program for lab 1 for reminders of how to use turtle graphics.

Functions that must be written
def drawLetter (x, y, letterColor):
Write three functions, one for three unique letters. Personally, I would write drawT, drawL, and
drawS. Each function must draw that letter to the screen. The x and y values determine the
upper left-hand location for the start of the letter. Ensure that each letter takes the same amount
of space, both vertically and horizontally. The letterColor parameter will be a string used to
determine the color of the letter – use it to set the fillcolor, and maybe pencolor. You can
also set pencolor to “black” to create an outline of the letter. In the Turtle Graphics Resources
link in blackboard I have a link to valid turtle graphic colors.

Each function can have one, and only one, goto command. If drawing a letter which requires
two “shapes,” such as a “O” with two circles you can use a second goto. The initial goto should
position the turtle in the upper left-hand location of the letter to be drawn. It would be best to not
make any assumption the direction of the turtle, to it would be smart to ensure that you know
what direction the turtle is pointing before starting to draw the letter. All of the actual drawing
must be done with basic movements, such as forward, backward, left, or right. Remember
to use penup and pendown to ensure you only draw the desired lines.

def drawShadowedLetter (x, y, letterColor, offset):
Write three more functions, one for each letter (mine would be drawShadowedT,
drawShadowedL, and drawShadowedS). These functions will use your drawLetter functions,
once using letterColor, and once adding offset to the x and y values and using “black” as
the color. This will create a “shadowed” letter. These three functions will not be doing any
actual drawing, all of the graphics work will be done in the drawLetter functions.

In the main program, draw your initials to the screen twice. The first time write your initials to the
screen using the drawLetter functions. Somewhere else on the display, write your initials to
the screen using the drawShadowedLetter functions.

Challenge – no points, just knowledge 
Write a function named drawName (x, y), which writes all the letters to the screen, evenly
spaced out. This will require a loop to access each letter in your name, as well as a variable to
determine the x, y location for each letter. You could even write drawHName(x, y) and
drawVName (x, y), which would write out your letters either horizontally or vertically, again
evenly spaced, using x and y as a starting location for the first letter.
'''

firstTurt = turtle.Turtle()


def drawJ(x, y, letterColor):

    # First goto to the first letter.

    firstTurt.pencolor(letterColor)
    firstTurt.begin_fill()
    firstTurt.fillcolor(letterColor)
    firstTurt.penup()
    firstTurt.setheading(120)  # Turtles gotta walk facing forward.
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


def drawW(x, y, letterColor):

    # Second goto to the second letter.

    firstTurt.pencolor(letterColor)
    firstTurt.begin_fill()
    firstTurt.fillcolor(letterColor)
    firstTurt.penup()
    firstTurt.setheading(0)  # Turtles gotta walk facing forward.
    firstTurt.goto(x, y)
    firstTurt.setheading(270)
    firstTurt.pendown()

    # Draw the W

    firstTurt.forward(200)
    firstTurt.left(90)
    firstTurt.forward(75)
    firstTurt.left(90)
    firstTurt.forward(50)
    firstTurt.right(90)
    firstTurt.forward(50)
    firstTurt.right(90)
    firstTurt.forward(50)
    firstTurt.left(90)
    firstTurt.forward(75)
    firstTurt.left(90)
    firstTurt.forward(200)
    firstTurt.left(90)
    firstTurt.forward(50)
    firstTurt.left(90)
    firstTurt.forward(100)
    firstTurt.right(90)
    firstTurt.forward(25)
    firstTurt.right(90)
    firstTurt.forward(50)
    firstTurt.left(90)
    firstTurt.forward(50)
    firstTurt.left(90)
    firstTurt.forward(50)
    firstTurt.right(90)
    firstTurt.forward(25)
    firstTurt.right(90)
    firstTurt.forward(100)
    firstTurt.left(90)
    firstTurt.forward(50)

    firstTurt.end_fill()


def drawG(x, y, letterColor):

    # Third goto to the third letter.

    firstTurt.pencolor(letterColor)
    firstTurt.begin_fill()
    firstTurt.fillcolor(letterColor)
    firstTurt.penup()
    firstTurt.setheading(0)  # Turtles gotta walk facing forward.
    firstTurt.goto(x, y)
    firstTurt.setheading(270)
    firstTurt.pendown()

    # Draw the G

    firstTurt.forward(200)
    firstTurt.left(90)
    firstTurt.forward(200)
    firstTurt.left(90)
    firstTurt.forward(125)
    firstTurt.left(90)
    firstTurt.forward(100)
    firstTurt.left(90)
    firstTurt.forward(50)
    firstTurt.left(90)
    firstTurt.forward(50)
    firstTurt.right(90)
    firstTurt.forward(25)
    firstTurt.right(90)
    firstTurt.forward(100)
    firstTurt.right(90)
    firstTurt.forward(100)
    firstTurt.right(90)
    firstTurt.forward(150)
    firstTurt.left(90)
    firstTurt.forward(50)
    firstTurt.left(90)
    firstTurt.forward(200)

    firstTurt.end_fill()


def drawshadowedJ(x, y, letterColor, offset):
    drawJ(x + offset, y + offset, 'black')
    drawJ(x, y, letterColor)


def drawshadowedW(x, y, letterColor, offset):
    drawW(x + offset, y + offset, 'black')
    drawW(x, y, letterColor)


def drawshadowedG(x, y, letterColor, offset):
    drawG(x + offset, y + offset, 'black')
    drawG(x, y, letterColor)


def main():
    scrn = turtle.Screen()
    scrn.setup(800, 1000)
    scrn.bgcolor("medium spring green")

    firstTurt.shape('triangle')
    firstTurt.shapesize(1, 1, 1)
    firstTurt.pensize(1)
    firstTurt.speed(4)

    drawJ(-300, 300, 'red')
    drawW(-100, 300, 'blue')
    drawG(150, 300, 'yellow')

    drawshadowedJ(-300, -100, 'yellow', 5)
    drawshadowedW(-100, -100, 'blue', 5)
    drawshadowedG(150, -100, 'red', 5)

    scrn.exitonclick()


main()
