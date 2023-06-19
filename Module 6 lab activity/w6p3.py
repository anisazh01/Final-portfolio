# Alina Zholdubaeva
# 06/04/2023
# w6p3.py
# The program uses random.choice to select a day of the week from a list and print that day.

import random

days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
random_day = random.choice(days_of_the_week)
print(random_day)