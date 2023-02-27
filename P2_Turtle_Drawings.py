print("This code displays some cool drawings using Turtle in Python.\n")

import turtle
turtle.bgcolor("Orange")
turtle.pensize(2)

# Drawing a Square using Turtle.

""" turtle.forward(150)
turtle.left(90)

turtle.forward(150)
turtle.left(90)

turtle.forward(150)
turtle.left(90)

turtle.forward(150)
turtle.left(90)

turtle.done() #This command is used to make the drawing board stay on the screen.
 """

# Drawing a circle.

for i in range(6):

    for i in ["Red", "Blue", "Green", "Yellow", "Black", "Cyan"]:
        turtle.color(i)
        turtle.circle(150)
        turtle.left(10)
        turtle.speed(500)
turtle.done()