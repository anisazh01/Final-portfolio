# Alina Zholdubaeva
# 06/18/2023
# p2.w9
# The program contains the numbers 0 to 10. On each iteration, the loop should append the current value of a counter variable to the list and then increase the counter by 1. The while loop should stop once the counter variable is greater than 10.

def make_list():
    L = []
    counter = 0

    while counter <= 10:
        L.append(counter)
        counter += 1

    return L

result_list = make_list()
print(result_list)
