#main_game.py
#Alina Zholdubaeva
#06/18/2023
#This file will control the rest of the game.

import section_1
import main_character

print("Hello there!")
print("Welcome to the game: Destination!")
print("This world is full of adventures.")
player = main_character.main_character()
player.name = input("Your character name is Lara.")
print("Welcome Lara!")
input("press Enter to start your game!")



section_1.start()


