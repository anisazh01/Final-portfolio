# Alina Zholdubaeva
# 06/18/2023
# The program that prints numbers from 1 to 50, applying the given conditions:

for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("Divisible by both")
    elif num % 3 == 0:
        print("Divisible by 3")
    elif num % 5 == 0:
        print("Divisible by 5")
    else:
        print(num)
