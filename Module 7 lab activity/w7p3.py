# Alina Zholdubaeva
# 06/04/2023
# w7p3
# The program multiplies all the numbers in a list. The function should
# take a list of numbers as a parameter and return the final result of the multiplication.

def multiplyListNumbers(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result