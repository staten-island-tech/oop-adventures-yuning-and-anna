from Roms.introduction_to_room import *

from Roms.roms import * 

from ChARActer.chARActer import *

from MOBS.mobsC import *

from MOBS.mobs_ import *

from Crying import *


def Mattack():
    HIT = MOB1.strength - ara_ara.defense
    ara_ara.health = ara_ara.health - HIT
    print(MOB1, "has dealt", HIT, "damage to", ara_ara)
    return ara_ara.health

def Mattack2():
    HIT = MOB2.strength - ara_ara.defense
    ara_ara.health = ara_ara.health - HIT
    print(MOB2, "has dealt", HIT, "damage to", ara_ara)
    return ara_ara.health

def Mattack3():
    HIT = MOB3.strength - ara_ara.defense
    ara_ara.health = ara_ara.health - HIT
    print(MOB3, "has dealt", HIT, "damage to", ara_ara)
    return ara_ara.health

def arack():
    ARAIT = Skills.arage
    MOB.health = MOB.health -  + MOB.thick_skin
    print(ara_ara, "has dealt", ARAIT, "damage to", MOB)

def arack2():
    ARAIT = Skills.arage
    MOB2.health = MOB2.health -  + MOB2.thick_skin
    print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)

def arack():
    ARAIT = Skills.arage
    MOB3.health = MOB3.health -  + MOB3.thick_skin
    print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)



def starting():
    beginning = input("Type start_adventure when are ready to begin ")
    if beginning == "start_adventure":
        print(intro_room_beginning)
    else:
        print("Try again when you are ready")
        beginning = input("Type start_adventure when are ready to begin ")
 
alreadyfoughten = []

def starting():
    beginning = input("Type start when are ready to begin ")
    if beginning == "start":
        print(intro_room_beginning)
    else:
        print("Try again when you are ready")
        beginning = input("Type start when are ready to begin ")

print("This is the best RPG game you will play in this period. So the story is probs a fantasy world and your character is trash. The whole game is about trying to level up from adventure rank F and also not to rage quit the game because of some great devs :). Anyways the game begins with MC becoming an adventurer but adventures start at rank F, how original. MC is a failure. But, from exploring life and beating monsters, and also getting beat by monsters, the MC can level up and not be a failure(L). ")


ara_ara = input("What do you want to name your character?") 

starting()

print("In this game, there are 5 different moves that you can use"
"They are punch, slash, explosive shot, armor pierce, and sword storm."
"Punch does 40 damage if the enemy has no defense and you don't need any weapons"
"Slash does the damage that your weapon has."
"Explosion Sot does the damage of your bow, but it takes 2 turns to use."
"Sword Storm does half the damage of your weapon, but it an an AOE attack, which will attack every enemy.")

def moves():
    print("In this game, there are 5 different movews that you can use"
"They are punch, slash, explosive shot, armor pierce, and sword storm."
"Punch does 40 damage if the enemy has no defense and you don't need any weapons"
"Slash does the damage that your weapon has."
"Explosion Sot does the damage of your bow, but it takes 2 turns to use."
"Sword Storm does half the damage of your weapon, but it an an AOE attack, which will attack every enemy.")
    MCchoice = input("What move do you want to use? Only type the first letter of the move.")
    if MCchoice == p:

    

currentRoom = room_1

if currentRoom == room_1:
    if "room1" in alreadyfoughten:    
        user_move_room_1()
    else: 
        MOB1 = slime
        MOB2 = slime 
        MOB3 = slime
        print(room_1beg)
        


        user_move_room_1()

