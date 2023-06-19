#section_1.py
#Alina Zholdubaeva
#06/18/2023
#This file will control the first section of the game.



from random import shuffle
import main_character
import section_2

def start():
    print("You're standing in the middle of a small town.")
    print("Seeking guidance? You should reach out to the knowledgeable owner of the souvenir store. His name is Peter.")
    print("He possesses invaluable expertise and can provide you with step-by-step instructions to navigate through each level of the game.")
    choice = input("Would you like to go to the Souvenir store? : ")
    if choice.lower() == 'yes' or choice.lower() == 'y':
        print("You enter the souvenir store.")

        responses = ["Hi! How can I help you? Would you like to talk with Peter?", "Are you looking for Peter?"]
        npcNameChoice = ["Audie", "Ryan", "Dawn"]

        shuffle(npcNameChoice)
        npcName = npcNameChoice[0]

        print(npcName, ":Hello, I am", npcName, ", will you talk to me?")
        shuffle(responses)
        answer = input("Press y to talk to the villager")
        if answer == "y":
            print(npcName, ":", responses[0])
        else:
            print(npcName, ":Do you want to talk with Peter?")

        second_answer = input("Press y to talk to the Peter")
        if second_answer == "y":
            print("Hi Peter! My name is Lara. I need your help. I am not from here. I need to go back home. Someone told me that you know how I can go back.")
            print(
                "Peter: Okay Lara. I will give you first instruction. Only after completing it. You can go to the next level. Overall, there is three levels. The first level requires you to find five bags of gold in the forest.")
        else:
            print("invalid choice")

        print("1. Forest")
        print("2. Weapon store")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("You enter the forest. Now it's time for you to find five bags of gold.")
            # The player enters the woods, where they need to find five bags of gold.
        elif choice == 2:
            print("You enter a weapon store, but you don't have money to buy anything right now.")



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

        print("Now you have enough bags of gold. You can exchange it to knives in the weapon store.")

    print("1. Forest")
    print("2. Weapon store")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("You enter the forest. You have already found bags of gold. Now you have to go to weapon store.")
        # The player enters the woods, where they need to find five bags of gold.
    elif choice == 2:
        print("You enter a weapon store.")

    choice = input("What would you like to buy? You can buy knives. ")
    if choice.lower() == 'knives':
        print(
            "Knives are short-bladed weapons designed for quick and precise attacks. They excel in close-quarters combat, allowing for swift slashes or stabs. Their lightweight nature often grants increased agility and stealth when used as a secondary weapon.")
        buy_choice = input("Would you like to buy? (Y/N): ")
        if buy_choice.lower() == 'y':
            print("You have purchased the knives.")
            section_2.start()
        elif buy_choice.lower() == 'n':
            print("You chose not to buy the knives. ")
        else:
            print("Invalid choice. To get instructions, you should talk to Peter.")
    else:
        print("Invalid choice. Please select a valid option.")



# main_character.start()



