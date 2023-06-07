from Roms.introduction_to_room import *

from Roms.roms import * 

from ChARActer.chARActer import *

from MOBS.mobsC import *

from MOBS.mobs_ import *

from Crying import *

from Nroom import *

 
alreadyfoughten = []

from MOBS.mobs_ import *


print("This is the best RPG game you will play in this period (cause it's the only one :) ). The whole game is about trying to level up from adventure rank F and also not to rage quit the game because of some great devs :) (Yunning not Anna). Anyways the game begins with MC becoming an adventurer but adventures start at rank F, how original. MC is a failure. But, from exploring life and beating monsters, and also getting beat by monsters, the MC can level up and not be a failure(L). ")


ara_ara = input("What do you want to name your character?") 

starting()

moveinfo()

if currentRoom == room_1:
    weapon_damage = 0
    firepower = 0
    if "room1" in alreadyfoughten:    
        everything_rooms_1()
    else: 
        MOBAM = 3
        MOB1 = slime
        MOB2 = slime 
        MOB3 = slime
        print(room_1beg)
        print("Mob 1 is a slime, Mob 2 is a slime, and Mob 3 is a slime.")
        MCchoice()
        



        everything_rooms_1()

if currentRoom == room_2:
    if "room2" in alreadyfoughten:    
        everything_rooms_2()
    else: 
        MOBAM = 3
        MOB1 = skeleton
        MOB2 = skeleton
        MOB3 = skeleton
        print(room_2beg)
        print("Mob 1 is a skeleton, Mob 2 is a skeleton, and Mob 3 is a skeleton.")
        MCchoice()


        everything_rooms_2()

if currentRoom == room_3:
    if "room3" in alreadyfoughten:    
        everything_rooms_3()
    else: 
        MOBAM = 3
        MOB1 = spider
        MOB2 = spider
        MOB3 = spider
        print(room_3beg)
        print("Mob 1 is a spider, Mob 2 is a spider, and Mob 3 is a spider.")
        MCchoice()


        everything_rooms_3()

if currentRoom == room_4:
    if "room4" in alreadyfoughten:    
        everything_room_4()
    else: 
        MONAM = 3
        MOB1 = orc
        MOB2 = slime 
        MOB3 = slime
        print(room_4beg)
        print("Mob 1 is a orc, Mob 2 is a slime, and Mob 3 is a slime.")
        MCchoice()


        everything_room_4()

if currentRoom == room_5:
    if "room5" in alreadyfoughten:    
        everything_rooms_5()
    else: 
        MOBAM = 3
        MOB1 = BiG_sLIME
        MOB2 = slime 
        MOB3 = slime
        print(room_5beg)
        print("Mob 1 is a big slime, Mob 2 is a slime, and Mob 3 is a slime.")
        MCchoice()


        everything_rooms_5()

if currentRoom == room_6:
    if "room6" in alreadyfoughten:    
        everything_rooms_6()
    else: 
        MOBAM = 3
        MOB1 = BiG_sLIME
        MOB2 = BiG_sLIME 
        MOB3 = slime
        print(room_6beg)
        print("Mob 1 is a big slime, Mob 2 is a big slime, and Mob 3 is a slime.")
        MCchoice()


        everything_rooms_6()


