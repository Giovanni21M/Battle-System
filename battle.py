from sys import exit
from random import randint


class Battle():

    characters = { 
        'hero' : { 
            'hp' : 10, 
            'attack' : randint(8,12),
            'defense' : 10
        },
        'minotaur' : { 
            'hp' : 13, 
            'attack' : randint(9,14),
            'defense' : 9
        }
    }

    def __init__(self, enemy_data):
        self.enemy_data = enemy_data

    def enemy_damage(self):
        enemy_atk = Battle.characters[self.enemy_data]['attack']
        player_def = Battle.characters['hero']['defense']

        if enemy_atk > player_def:
            enemy_dps = enemy_atk - player_def
            Battle.characters['hero']['hp'] -= enemy_dps
            print("Hero HP is now: ", Battle.characters['hero']['hp'])
        else:
            Battle.characters['hero']['hp'] -= 1

    def player_damage(self):
        player_atk = Battle.characters['hero']['attack']
        enemy_def = Battle.characters[self.enemy_data]['defense']

        if player_atk > enemy_def:
            player_dps = player_atk - enemy_def
            Battle.characters[self.enemy_data]['hp'] -= player_dps
        else:
            Battle.characters[self.enemy_data]['hp'] -= 1


# Start testing here

print("~~~~~~~~~~~~~~~~~~~~~")
print("Battle test commence!")
print("~~~~~~~~~~~~~~~~~~~~~")
print("\nHero HP: ", Battle.characters['hero']['hp'])
print("Enemy HP: ", Battle.characters['minotaur']['hp'])



while (Battle.characters['hero']['hp'] >= 0) or (Battle.characters['minotaur']['hp'] >= 0):

    dmg = Battle('minotaur')

    choice = input("\n1. Attack or 2. Run  >> ")
    choice = choice.lower()

    if (choice == "1") or (choice == "attack"):
        print("\nYou swiftly attack.")
        dmg.player_damage()
        print("Enemy HP: ", Battle.characters['minotaur']['hp'])
    elif (choice == "2") or (choice == "run"):
        print("\nYou fail to run away and get hit.")
        dmg.enemy_damage()
        print("Your HP: ", Battle.characters['hero']['hp'])
    else:
        print("\nYou failed to make a decision and sustained damage.")
        dmg.enemy_damage()
        print("Your HP: ", Battle.characters['hero']['hp'])

    if Battle.characters['hero']['hp'] <= 0:
        print("You have been defeated.")
        exit(1)
    elif Battle.characters['minotaur']['hp'] <= 0:
        print("You have defeated the enemy.")
        exit(1)
