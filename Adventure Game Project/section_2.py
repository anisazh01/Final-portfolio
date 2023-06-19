#section_2.py
#Alina Zholdubaeva
#06/18/2023
#This file will control the second section of the game.

import section_3
import main_character
def start():
    print("Section 2")
    print("You enter the Souvenir store. Now you need to talk with Peter.")
    choice = input("Would you like to speak with him? (Y/N): ")
    if choice.lower() == "y":
        print("Hi Peter! I have found five bags of gold and exchanged them for knives. What's next?")
        print("Peter: Good job, Lara! You have completed the first level of the game. Now into the second part. The second level requires you to find eight bags of gold. In this section, monsters will appear and attempt to kill you.")
    else:
        print("You should talk to him.")

    print("1. Forest")
    print("2. Weapon store")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("You enter the forest. Now it's time for you to find eight bags of gold.")
        # The player enters the woods, where they need to find five bags of gold.
    elif choice == 2:
        print("You enter a weapon store, but you don't have money to buy anything right now.")

    # class bagofGold:
    #     def __init__(self):
    #         self.gold = 0
    #
    #     def add_gold(self, amount):
    #         self.gold += amount
    #         print(f"You collected {amount} bags of gold. Total gold in the bag: {self.gold}")

    # Create an instance of the bag
    #bag = bagofGold()

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
    weaponstore()
#start()




def weaponstore():
    print("Now you have enough bags of gold. You can exchange them for more advanced weapons in the store.")
    choice = int(input("Weapon store: What would you like to buy? 1. Rifles 2. Pistols"))
    if choice == 1:
        print("Rifles are long-barreled firearms with a stock that is braced against the shoulder for stability. They are typically fired from the shoulder and have a higher accuracy and longer effective range compared to handguns.")
    elif choice == 2:
        print("Pistols are compact firearms designed to be operated with one hand. They are commonly used as sidearms or for close to medium-range combat.")
    else:
        print("Choose from the options above!")

    buy_choice = input("Would you like to buy? (Y/N): ")
    if buy_choice.lower() == 'y':
        print("You have purchased the pistols.")
        section_3.start()
    elif buy_choice.lower() == 'n':
        print("You choose not to buy the rifles.")
    else:
        print("Invalid choice. Please select a valid option.")






