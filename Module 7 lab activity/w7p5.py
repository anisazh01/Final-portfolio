# Alina Zholdubaeva
# 06/04/2023
# w7p5
# Write a program with the following chunk of code. Modify this code to produce the
# image shown on the right:

import turtle

def drawSquare (t, sz):
    """Get turtle t to draw a square of sz side"""
    for i in range (4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
alex =  turtle.Turtle()
alex.color("blue")

# Move the turtle to the starting position
alex.penup()
alex.goto(-50, -50)
alex.pendown()


drawSquare(alex, 200)


alex.penup()
alex.goto(-20, -20)
alex.pendown()
drawSquare(alex, 140)


alex.penup()
alex.goto(-10, -10)
alex.pendown()
drawSquare(alex, 120)

alex.penup()
alex.goto(0, 0)
alex.pendown()
drawSquare(alex, 100)

wn.exitonclick()