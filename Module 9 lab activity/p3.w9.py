# Alina Zholdubaeva
# 06/18/2023
# p3.w9
# The program asks the user to enter a number. Append each entered number to a list and add them together. Continue asking for a number until the sum of the list of numbers is greater than 100.


def sum_numbers():
    num = []
    total_sum = 0

    while total_sum <= 100:
        user_input = float(input("Enter a number: "))
        num.append(user_input)
        total_sum = sum(num)

    return num, total_sum

result_list, result_sum = sum_numbers()
print("List of numbers:", result_list)
print("Sum of numbers:", result_sum)
