# Alina Zholdubaeva
# 06/04/2023
# w6p5.py
# The program takes two user inputs, a and b, and uses them to calculate the Pythagorean theorem using the sqrt() and pow() functions found in the math module.

import math

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))

c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

print("The value of c is:", c)