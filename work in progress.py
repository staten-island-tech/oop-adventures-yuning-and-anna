from Roms.introduction_to_room import *

from Roms.roms import * 

from ChARActer.chARActer import *

from MOBS.mobsC import *

from Crying import *
alreadyfoughten = ["room1"]

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

CurrentRoom = room_1

if CurrentRoom == room_1:
    if "room1" in alreadyfoughten:
        user_move_room_1()
    else: 
        print("hi")