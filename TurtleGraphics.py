import turtle

scrn = turtle.Screen() #essentially the paper we will draw on 
scrn.setup (800, 600) #set the size of the screen
scrn.bgcolor ("light grey") #turtle graphic resources on blackground & sites, look at

firstTurt = turtle.Turtle() #creates a "turtle"

firstTurt.pensize (5)
firstTurt.speed (1) #0 is instant and then 1-10 slow to fast
firstTurt.pencolor ('black')

#draws an black square
#to fill a shape do this before starting to draw the shape
firstTurt.begin_fill()
firstTurt.fillcolor ('black')

firstTurt.penup()
firstTurt.goto (-98, 98)
firstTurt.setheading(0)
firstTurt.pendown()

firstTurt.forward (100)
firstTurt.left (90)
firstTurt.forward (100)
firstTurt.left (90)

firstTurt.forward (100)
firstTurt.left (90)
firstTurt.forward (100)

#to do the actual filling of the shape do this when you are done drawing
#still will fill correctly even if you don't close the box completely
firstTurt.end_fill()

firstTurt.pensize (5)
firstTurt.speed (1) #0 is instant and then 1-10 slow to fast
firstTurt.pencolor ('forest green')

#draws an orange square
#to fill a shape do this before starting to draw the shape
firstTurt.begin_fill()
firstTurt.fillcolor ('orange')

firstTurt.penup()
firstTurt.goto (-100, 100)
firstTurt.setheading(0)
firstTurt.pendown()

firstTurt.forward (100)
firstTurt.left (90)
firstTurt.forward (100)
firstTurt.left (90)

firstTurt.forward (100)
firstTurt.left (90)
firstTurt.forward (100)

#to do the actual filling of the shape do this when you are done drawing
#still will fill correctly even if you don't close the box completely
firstTurt.end_fill()

firstTurt.hideturtle()

scrn.exitonclick() #has to be last