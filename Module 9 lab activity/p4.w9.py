# Alina Zholdubaeva
# 06/18/2023
# p4.w9
# The program creates a while loop that initializes a counter at 0 and will run until the counter reaches 50. If the value of the counter is divisible by 10, append the value to the list called tens. Confirm the list results using a print statement.

def create_tens():
    counter = 0
    tens = []

    while counter <= 50:
        if counter % 10 == 0:
            tens.append(counter)
        counter += 1

    return tens

result_list = create_tens()
print("List of numbers divisible by 10:", result_list)
