from sys import exit
from random import randint


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




def enemy_damage(enemy_data):
    enemy_atk = characters[enemy_data]['attack']
    player_def = characters['hero']['defense']

    if enemy_atk > player_def:
        enemy_dps = enemy_atk - player_def
        characters['hero']['hp'] = characters['hero']['hp'] - enemy_dps
        print("Hero HP is now: ", characters['hero']['hp'])
    else:
        characters['hero']['hp'] = characters['hero']['hp'] - 1

def player_damage(enemy_data):
    player_atk = characters['hero']['attack']
    enemy_def = characters[enemy_data]['defense']

    if player_atk > enemy_def:
        player_dps = player_atk - enemy_def
        characters[enemy_data]['hp'] = characters[enemy_data]['hp'] - player_dps
    else:
        characters[enemy_data]['hp'] = characters[enemy_data]['hp'] - 1


print("~~~~~~~~~~~~~~~~~~~~~")
print("Battle test commence!")
print("~~~~~~~~~~~~~~~~~~~~~")
print("\nHero HP: ", characters['hero']['hp'])
print("Enemy HP: ", characters['minotaur']['hp'])



while (characters['hero']['hp'] >= 0) or (characters['minotaur']['hp'] >= 0):

    choice = input("\n1. Attack or 2. Run  >> ")
    choice = choice.lower()

    if (choice == "1") or (choice == "attack"):
        print("\nYou swiftly attack.")
        player_damage('minotaur')
        print("Enemy HP: ", characters['minotaur']['hp'])
    elif (choice == "2") or (choice == "run"):
        print("\nYou fail to run away and get hit.")
        enemy_damage('minotaur')
        print("Your HP: ", characters['hero']['hp'])
    else:
        print("\nYou failed to make a decision and sustained damage.")
        enemy_damage('minotaur')
        print("Your HP: ", characters['hero']['hp'])

    if characters['hero']['hp'] <= 0:
      print("You have been defeated.")
      exit(1)
    elif characters['minotaur']['hp'] <= 0:
      print("You have defeated the enemy.")
      exit(1)
