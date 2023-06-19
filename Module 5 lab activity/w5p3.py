# Alina Zholdubaeva
# 06/18/2023
# The program uses a for loop and the turtle module to do the following:

import turtle


side_length = int(input("Enter the length of a side: "))
fill_color = input("Enter the fill color: ")
shape = input("Enter the shape (triangle or square): ")


screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.speed(2)
pen.color("black", fill_color)
pen.begin_fill()


if shape == "triangle":
    for _ in range(3):
        pen.forward(side_length)
        pen.left(120)
else:
    for _ in range(4):
        pen.forward(side_length)
        pen.left(90)

pen.end_fill()


turtle.done()
