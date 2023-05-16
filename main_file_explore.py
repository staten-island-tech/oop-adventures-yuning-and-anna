from Roms.introduction_to_room import *

from Roms.roms import * 

from ChARActer.chARActer import *

from MOBS.mobsC import *

from MOBS.mobs_ import *

def Mattack():
    HIT = MOB.strength - ara_ara.defense
    ara_ara.health = ara_ara.health - HIT
     

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
    Mobs_in = attacking


    
     

