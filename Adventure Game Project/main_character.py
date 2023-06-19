##main_character.py
#Alina Zholdubaeva
#06/18/2023
#This file will provide with the information about main character.

import random

class main_character:
    name = "Lara"
    level = 0
    bag = []
    attack = 5
    gold = 0
    inventory = []
    def add_gold(self,amount):
        self.gold += amount
        print(f"You collected {amount} bags of gold. Total gold in the bag: {self.gold}")
global Lara
Lara = main_character()

class Character:
    def __init__(self, name, hit_points, is_poisoned):
        self.name = name
        self.hit_points = hit_points
        self.is_poisoned = is_poisoned


    def take_damage(self,damage):
        # The character will take a random amount of damage between 1 and 5
        # If the character is already poisoned, they will take 3 extra damage
        if self.is_poisoned:
            damage = damage + 3
            self.hit_points -= damage
            return damage
        else:
            #damage = random.randint(1, 5)
            self.hit_points -= damage
            return damage



def fight(player, monster):
    print("A fierce battle begins between", player.name, "and the monster!")

    while player.hit_points > 0 and monster.hit_points > 0:
        # Player attacks the monster
        player_damage = random.randint(1, 6)
        monster.take_damage(player_damage)#hit_points -= player_damage
        print(player.name, "attacks the monster for", player_damage, "damage.")

        # Check if the monster is defeated
        if monster.hit_points <= 0:
            print("Congratulations! You defeated the monster!")
            break

        # Monster attacks the player
        monster_damage = random.randint(1,6)#take_damage(player)
        player.take_damage(monster_damage)
        print("The monster attacks", player.name, "for", monster_damage, "damage.")

        # Check if the player is defeated
        if player.hit_points <= 0:
            print("Oh no! You were defeated by the monster!")
            break






#fight(player, monster)