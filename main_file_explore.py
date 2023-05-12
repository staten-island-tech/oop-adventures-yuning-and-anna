from introduction_to_room import *

from roms import * 

from chARActer import *

def 

def attacking(ara_ara, monster, move):
    damage = ara_ara["move"][move]
    monster["defender"] = max(0, monster["health"] - damage)
    print(f"{ara_ara['name']} used {move} and dealt {damage} damage to {monster['name']}")

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


    
     

