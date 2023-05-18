from Roms.introduction_to_room import *

from Roms.roms import * 

from ChARActer.chARActer import *

from MOBS.mobsC import *

def starting():
    beginning = input("Type start_adventure when are ready to begin ")
    if beginning == "start_adventure":
        print(intro_room_beginning)
    else:
        print("Try again when you are ready")
        beginning = input("Type start_adventure when are ready to begin ")

ara_ara = input("WHaT do you wAnt to nAme your chARActer?") 


