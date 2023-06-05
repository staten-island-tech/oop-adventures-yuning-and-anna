from Roms.introduction_to_room import *

from Roms.roms import * 

from ChARActer.chARActer import *

from MOBS.mobsC import *

from MOBS.mobs_ import *

from Crying import *
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

print("In this game, there are 5 different movews that you can use"
"They are punch, slash, explosive shot, armor pierce, and sword storm."
"Punch does 40 damage if the enemy has no defense and you don't need any weapons")

CurrentRoom = room_7

if CurrentRoom == room_7:
    if "room7" in alreadyfoughten:    
        user_move_room_7()
    else: 
        MOB1 = BiG_sLIME
        MOB2 = BiG_sLIME 
        MOB3 = BiG_sLIME
        print(room_7beg)

        user_move_room_7()

if CurrentRoom == room_8:
    if "room8" in alreadyfoughten:    
        user_move_room_8()
    else: 
        MOB1 = skeleton
        MOB2 = orc
        print(room_8beg)

        user_move_room_8()

if CurrentRoom == room_9:
    if "room9" in alreadyfoughten:    
        user_move_room_9()
    else: 
        MOB1 = skeleton
        MOB2 = skeleton
        MOB3 = orc
        MOB4 = orc
        print(room_9beg)

        user_move_room_9()

if CurrentRoom == 