from introduction_to_room import *

from roms import * 

from chARActer import *

def attacking(attacker, defender, move):
    damage = attacker["move"][move]
    defender["defender"] = max(0, defender["health"] - damage)
    print(f"{attacker['name']} used {move} and dealt {damage} damage to {defender['name']}")

def starting():
    beginning = input("Type start_adventure when are ready to begin ")
    if beginning == "start_adventure":
        print(intro_room_beginning)
    else:
        print("Try again when you are ready")
        beginning = input("Type start_adventure when are ready to begin ")
 
def room_1():
    print(room_1)
    Mobs_in = Room_1


    
     

