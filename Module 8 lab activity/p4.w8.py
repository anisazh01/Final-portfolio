# Alina Zholdubaeva
# 06/18/2023
# The program takes a year as a parameter and returns True if the year is a leap year, False if it is otherwise.

def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

input_year = int(input("Enter a year: "))
result = is_leap_year(input_year)
print(result)
