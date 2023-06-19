# Alina Zholdubaeva
# 06/18/2023
# The program takes two inputs from a user and prints whether the sum is greater than 10, less than 10, or equal to 10.

def takes_inputs():
    input1=float(input("Enter the first value: "))
    input2 = float(input("Enter the second value: "))
    total_sum = input1+input2

    if total_sum > 10:
        print("The sum is greater than 10.")
    elif total_sum < 10:
        print("The sum is less than 10.")
    else:
        print ("The sum is equal to 10. ")

takes_inputs()
