from Roms.introduction_to_room import *

from Roms.roms import * 

from ChARActer.chARActer import *

from MOBS.mobsC import *

from MOBS.mobs_ import *

from Crying import *

from Nroom import *
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


if currentRoom == room_7:
    if "room7" in alreadyfoughten:    
        everything_rooms_7()
    else: 
        MOBAM = 3
        MOB1 = BiG_sLIME
        MOB2 = BiG_sLIME
        MOB3 = BiG_sLIME
        print(room_7beg)
        print("Mob 1 is a big slime, Mob 2 is also big slime, and Mob 3 is another big slime.")
        MCchoice()

if currentRoom == room_8:
    if "room8" in alreadyfoughten:    
        everything_rooms_8()
    else: 
        MOBAM = 2
        MOB1 = skeleton
        MOB2 = orc
        print(room_8beg)
        print("Mob 1 is a armored skely, Mob 2 is also a amoured orc.")
        MCchoice()

if currentRoom == room_9:
    if "room9" in alreadyfoughten:    
        everything_rooms_9()
    else: 
        MOBAM = 4
        MOB1 = skeleton
        MOB2 = skeleton
        MOB3 = orc
        MOB4 = orc
        print(room_9beg)
        print("Mob 1 is a skeley, Mob 2 is also skeley, and Mob 3 is another orc, plus mob 4 is another orc.")
        MCchoice()


if currentRoom == 'CRY_PEASANTS':
    everything_peasants()