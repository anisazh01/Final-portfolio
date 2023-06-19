#section_3.py
#Alina Zholdubaeva
#06/18/2023
#This file will control the third section of the game.

import main_character
# class BagOfGold:
#     def __init__(self):
#         self.gold = 0
#
#     def add_gold(self, amount):
#         self.gold += amount
#         print(f"You collected {amount} bags of gold. Total gold in the bag: {self.gold}")


def start():
    print("Section 3")
    print("You enter the Souvenir store. Now you need to talk with Peter.")
    choice = input("Would you like to speak with him? (Y/N): ")
    if choice.lower() == "y":
        print("Hi Peter! I have found eight bags of gold and exchanged them for a more advanced weapon. What's next?")
        print("Peter: Good job, Lara! You have completed the second level of the game. Now into the third part. The third level requires you to find ten bags of gold. In this section, more monsters will appear and attempt to kill you.")
    else:
        print("You should talk to him.")

    print("1. Forest")
    print("2. Weapon store")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("You enter the forest. Now it's time for you to find ten bags of gold.")
        # The player enters the woods, where they need to find ten bags of gold.
    elif choice == 2:
        print("You enter a weapon store, but you don't have money to buy anything right now.")

    # class bagofGold:
    #     def __init__(self):
    #         self.gold = 0
    #
    #     def add_gold(self, amount):
    #         self.gold += amount
    #         print(f"You collected {amount} bags of gold. Total gold in the bag: {self.gold}")
    #
    # # Create an instance of the bag
    # bag = bagofGold()

    # Simulation of collecting bags of gold

    while True:
        choice = input("Press 'c' to collect a bag of gold, or 'q' to quit: ")
        if choice.lower() == 'c':
            main_character.Lara.add_gold(1)
        elif choice.lower() == 'q':
            break
        else:
            print("Invalid choice. Try again.")
    player = main_character.Character(name="Lara", hit_points=20, is_poisoned=False)
    monster = main_character.Character(name="Goblin", hit_points=15, is_poisoned=False)
    main_character.fight(player,monster)
    start2()


def start2():
    print("Now you have enough bags of gold. You have to meet with Peter.")

    print("1. Souvenir store")
    print("2. Weapon store")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("You enter the souvenir store. Now you need to talk with Peter.")
        # The player enters the woods, where they need to find ten bags of gold.
    elif choice == 2:
        print("You enter a weapon store, but you have to go back home.")

    choice = input("Would you like to speak with him? (Y/N): ")

    if choice.lower() == "y":
        print("Hi Peter! I have found ten bags of gold and brought them to you. You said it is the final round. What's next?")
        print("Peter: Congratulations! You have completed the final level of the game. Now you can take this book. Once you open it, you will be in another reality.")
    else:
        print("You should talk to him.")

    choice = input("Would you like to open this book? (Y/N): ")

    if choice.lower() == "y":
        print("Now you are back home :)")
    else:
        print("You can reset this game")

#start()








