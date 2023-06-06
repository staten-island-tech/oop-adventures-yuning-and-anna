from Roms.introduction_to_room import *

from Roms.roms import * 

from ChARActer.chARActer import *

from MOBS.mobsC import *

from MOBS.mobs_ import *

from Crying import *

from Nroom import *


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

from MOBS.mobs_ import *



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
        ARAIT = 40


    

currentRoom = room_1

if currentRoom == room_1:
    if "room1" in alreadyfoughten:    
        everything_rooms_1()
    else: 
        MOB1 = slime
        MOB2 = slime 
        MOB3 = slime
        print(room_1beg)
        


        everything_rooms_1()

if currentRoom == room_2:
    if "room2" in alreadyfoughten:    
        everything_rooms_2()
    else: 
        MOB1 = skeleton
        MOB2 = skeleton
        MOB3 = skeleton
        print(room_2beg)
        


        everything_rooms_2()

if currentRoom == room_3:
    if "room3" in alreadyfoughten:    
        everything_rooms_3()
    else: 
        MOB1 = spider
        MOB2 = spider
        MOB3 = spider
        print(room_3beg)
        


        everything_rooms_3()

if currentRoom == room_4:
    if "room4" in alreadyfoughten:    
        everything_room_4()
    else: 
        MOB1 = orc
        MOB2 = slime 
        MOB3 = slime
        print(room_4beg)
        


        everything_room_4()

if currentRoom == room_5:
    if "room5" in alreadyfoughten:    
        everything_rooms_5()
    else: 
        MOB1 = BiG_sLIME
        MOB2 = slime 
        MOB3 = slime
        print(room_5beg)
        


        everything_rooms_5()

if currentRoom == room_6:
    if "room6" in alreadyfoughten:    
        everything_rooms_6()
    else: 
        MOB1 = BiG_sLIME
        MOB2 = BiG_sLIME 
        MOB3 = slime
        print(room_6beg)
        


        everything_rooms_6()


