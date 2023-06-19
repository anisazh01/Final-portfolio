# Alina Zholdubaeva
# 06/04/2023
# w7p4
# The program takes a list of numbers and returns a new list with
# unique elements of the first list.

def getUniqueElements(numbers):
    unique_list = []
    for number in numbers:
        if number not in unique_list:
            unique_list.append(number)
    return unique_list

#example
my_list = [1, 3, 3, 3, 6, 2, 3, 5]
result = getUniqueElements(my_list)
print(result)