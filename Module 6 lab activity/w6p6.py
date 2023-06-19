# Alina Zholdubaeva
# 06/04/2023
# w6p6.py
# The program takes a number from a user and calculates the factorial of that number in two ways:

import math

# Using a for loop
number = int(input("Enter a number: "))
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Factorial using a for loop:", factorial)

# Using the math module
number = int(input("Enter a number: "))
factorial = math.factorial(number)

print("Factorial using the math module:", factorial)