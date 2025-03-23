#Square with turtle
import turtle
turtle.Screen().bgcolor("yellow")
turtle.Screen().setup(300,400)
square = turtle.Turtle()
turtle.speed(1)
num_sides = 4
angle = 360.0/num_sides

for i in range (num_sides):
    square.forward(100)
    square.left(90)

turtle.done()
