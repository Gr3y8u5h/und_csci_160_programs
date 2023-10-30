'''
JWGTurtle.py - Lab 1 - CS160 Computer Science 1 Online - by: Joshua George.

Instructions are as follows;

Using Turtle Graphics, write your initials, or any other combination of 3 unique letters to the 
screen.  Do not draw the letters using simple lines, even thick lines, you need to draw an outline 
of the letter which can then be filled. Fill each letter with a color different from the color of the 
outline. Have a comment before starting the code for each letter indicating the letter that is to 
be drawn. It doesn’t have to be complicated, just something like: #draw T

Requirements 
You may only use goto() once per letter in your drawings, meaning you can use goto() 
before starting to draw each letter. A second use of goto() per letter is allow if you need two 
separate, unconnected lines, such as drawing an “O”. To do this I drew the “outer” line, filled it 
with a color (white in my example), then drew the “inner” line and filled it with the color of the 
background (light gray in my example). The actual drawing must be done using forward() 
and/or backward(). Finish each letter by filling it with a unique color. 

Make sure to comment both files, using multiline comments to document the file and single 
line comments to document the various “sections” of code within the file.

'''
### Importing the turtle library and setting the screen and background color.

import turtle

scrn = turtle.Screen() 
scrn.setup (800, 400) 
scrn.bgcolor ("Medium Blue") 

### Setting up the globals on the first turtle.

firstTurt = turtle.Turtle() 
firstTurt.shape('turtle')
firstTurt.shapesize(2,2,1)
firstTurt.pensize(5)
firstTurt.speed(1)

###  First goto to the first letter.

firstTurt.pencolor ('light grey')
firstTurt.begin_fill()
firstTurt.fillcolor ('green')
firstTurt.penup()
firstTurt.setheading(135)  ###  Turtles gotta walk facing forward.
firstTurt.goto (-150, 100)
firstTurt.setheading(180)
firstTurt.pendown()

### Draw the J

firstTurt.forward (150)
firstTurt.left (90)
firstTurt.forward (50)
firstTurt.left (90)
firstTurt.forward (50)
firstTurt.right (90)
firstTurt.forward (100)
firstTurt.right (90)
firstTurt.forward (50)
firstTurt.right (90)
firstTurt.forward (50)
firstTurt.left (90)
firstTurt.forward (50)
firstTurt.left (90)
firstTurt.forward (100)
firstTurt.left (90)
firstTurt.forward (150)
firstTurt.left (90)
firstTurt.forward (150)
firstTurt.right (90)
firstTurt.forward (50)
firstTurt.left (90)
firstTurt.forward (50)

firstTurt.end_fill()

###  Second goto to the second letter.

firstTurt.pencolor ('violet') 
firstTurt.begin_fill()
firstTurt.fillcolor ('red')
firstTurt.penup()
firstTurt.setheading(0)  ###  Turtles gotta walk facing forward.
firstTurt.goto (-100, 100)
firstTurt.setheading(270)
firstTurt.pendown()

### Draw the W

firstTurt.forward (200)
firstTurt.left (90)
firstTurt.forward (75)
firstTurt.left (90)
firstTurt.forward (50)
firstTurt.right (90)
firstTurt.forward (50)
firstTurt.right (90)
firstTurt.forward (50)
firstTurt.left (90)
firstTurt.forward (75)
firstTurt.left (90)
firstTurt.forward (200)
firstTurt.left (90)
firstTurt.forward (50)
firstTurt.left (90)
firstTurt.forward (100)
firstTurt.right (90)
firstTurt.forward (25)
firstTurt.right (90)
firstTurt.forward (50)
firstTurt.left (90)
firstTurt.forward (50)
firstTurt.left (90)
firstTurt.forward (50)
firstTurt.right (90)
firstTurt.forward (25)
firstTurt.right (90)
firstTurt.forward (100)
firstTurt.left (90)
firstTurt.forward (50)

firstTurt.end_fill()

###  Third goto to the third letter.

firstTurt.pencolor ('cadet blue') 
firstTurt.begin_fill()
firstTurt.fillcolor ('dark violet')
firstTurt.penup()
firstTurt.setheading(0)  ###  Turtles gotta walk facing forward.
firstTurt.goto (150, 100)
firstTurt.setheading(270)
firstTurt.pendown()

### Draw the G

firstTurt.forward (200)
firstTurt.left (90)
firstTurt.forward (200)
firstTurt.left (90)
firstTurt.forward (125)
firstTurt.left (90)
firstTurt.forward (100)
firstTurt.left (90)
firstTurt.forward (50)
firstTurt.left (90)
firstTurt.forward (50)
firstTurt.right (90)
firstTurt.forward (25)
firstTurt.right (90)
firstTurt.forward (100)
firstTurt.right (90)
firstTurt.forward (100)
firstTurt.right (90)
firstTurt.forward (150)
firstTurt.left (90)
firstTurt.forward (50)
firstTurt.left (90)
firstTurt.forward (200)

firstTurt.end_fill()

###  An extra goto for 5h1t$ and giggles.

firstTurt.penup()
firstTurt.setheading(230)  ###  Turtles gotta walk facing forward.
firstTurt.fillcolor('Green Yellow')
firstTurt.goto(0,-25)

###  Doing a celebratory spin.

firstTurt.setheading(270)  
firstTurt.setheading(0)
firstTurt.setheading(90)
firstTurt.setheading(180)
firstTurt.setheading(270)
firstTurt.stamp()

###  Self explanatory, second "turdle".

turd = turtle.Turtle()
turd.fillcolor ('saddle brown')
turd.shape('circle')
turd.shapesize(1,1,1)
turd.pensize(2)
turd.speed(1)

scrn.exitonclick()