from Roms.introduction_to_room import *

from Roms.roms import * 

from ChARActer.chARActer import *

from MOBS.mobsC import *

from MOBS.mobs_ import *

from Nroom import *

from RNG_SADGE.freebies import *

from RNG_SADGE.rng import *

def starting(): 
    beginning = input("Type start when are ready to begin ")
    if beginning == "start":
        print(intro_room_beginning)
    else:
        print("Try again when you are ready")
        beginning = input("Type start when are ready to begin ")

def Mattack1():
    global aralth
    HIT = power1 - araprotect
    aralth = aralth - HIT
    print("Mob 1 has dealt", HIT, "damage to", ara_ara)
    print(ara_ara, "has", aralth,"left")

def Mattack2():
    global aralth
    HIT = power2 - araprotect
    aralth = aralth - HIT
    print("Mob 2 has dealt", HIT, "damage to", ara_ara)
    print(ara_ara, "has", aralth,"left")

def Mattack3():
    global aralth
    HIT = power3 - araprotect
    aralth = aralth - HIT
    print("Mob 3 has dealt", HIT, "damage to", ara_ara)
    print(ara_ara, "has", aralth,"left")

def Mattack4():
    global aralth
    HIT = power4 - araprotect
    aralth = aralth - HIT
    print("Mob 4 has dealt", HIT, "damage to", ara_ara)
    print(ara_ara, "has", aralth,"left")

def moveinfo():
    print("In this game, there are 5 different moves that you can use"
    "They are punch, slash, explosive shot, armor pierce, and air cutter."
    "Punch does 40 damage if the enemy has no defense and you don't need any weapons"
    "Slash does the damage of your weapon, so if you don't have a weapon, it does no damage."
    "Explosive shot does the damage of your bow, so if you don't have a bow, it does no damage. Additionally, this move takes two rounds, so plan accordingly."
    "Lastly, Air Cutter is an AOE type of move, so it attacks all enemies. It does half the damage of your weapon, so if you don't have a weapon, it does no damage.")

def matack3():
    if "mob1" in imagine and "mob2" in imagine:
        Mattack3()
    elif "mob3" in imagine and "mob2" in imagine:
        Mattack1()
    elif "mob1" in imagine and "mob3" in imagine:
        Mattack2()
    elif "mob1" in imagine:
        Mattack2()
        Mattack3()
    elif "mob2" in imagine:
        Mattack1()
        Mattack3()
    elif "mob3" in imagine:
        Mattack1()
        Mattack2()
    else:
        Mattack1()
        Mattack2()
        Mattack3()

def matack4():
    if "123" in imagine:
        Mattack4()
    elif "234" in imagine:
        Mattack1()
    elif "341" in imagine:
        Mattack2()
    elif "412" in imagine:
        Mattack3()
    elif "12" in imagine:
        Mattack3()
        Mattack4()
    elif "13" in imagine:
        Mattack2()
        Mattack4()
    elif "14" in imagine:
        Mattack3()
        Mattack2()
    elif "23" in imagine:
        Mattack1()
        Mattack4()
    elif "24" in imagine:
        Mattack3()
        Mattack1()
    elif "34" in imagine:
        Mattack1()
        Mattack2()
    elif "1" in imagine:
        Mattack2()
        Mattack3()
        Mattack4()
    elif "2" in imagine:
        Mattack1()
        Mattack3()
        Mattack4()
    elif "3" in imagine:
        Mattack2()
        Mattack1()
        Mattack4()
    elif "4" in imagine:
        Mattack2()
        Mattack3()
        Mattack1()
    else:
        Mattack2()
        Mattack3()
        Mattack1()
        Mattack4()

def matack2():
    if "1" in imagine:
        Mattack2()
    elif "2" in imagine:
        Mattack1()
    else:
        Mattack1()
        Mattack2()
 
alreadyfoughten = []


print("This is the best RPG game you will play in this period (cause it's the only one :) ). The whole game is about trying to level up from adventure rank F and also not to rage quit the game because of some great devs :) (Yunning not Anna). Anyways the game begins with MC becoming an adventurer but adventures start at rank F, how original. MC is a failure. But, from exploring life and beating monsters, and also getting beat by monsters, the MC can level up and not be a failure(L). ")


ara_ara = input("What do you want to name your character?") 

starting()

moveinfo()

currentRoom = 1

if currentRoom == 1:
    weapon_damage = 0
    firepower = 0
    if "room1" in alreadyfoughten:    
        everything_rooms_1()
    else:
        imagine = []
        MOB1 = slime
        MOB2 = slime 
        MOB3 = slime
        vigor1 = 200
        vigor2 = 200
        vigor3 = 200
        power1 = 10
        power2 = 10
        power3 = 10
        protection1 = 5
        protection2 = 5
        protection3 = 5
        MOBAM = 3
        def MCchoice():
            vigor1 = 200
            vigor2 = 200
            vigor3 = 200
            moveinfo()
            CHOICE = input("What move do you want to use? Only type the first letter (lowercase) of the move that you want")
            if CHOICE == "p":
                ARAIT = int(60)
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            global vigor1
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to Mob 1")
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            global vigor2
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to Mob 2")
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            global vigor3
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to Mob 3")
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                        CHOICE = input("What move do you want to use? Only type the first letter (lowercase) of the move that you want")

                Mobchoice()
            elif CHOICE == "e":
                ARAIT = firepower
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            global vigor1
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            global vigor2
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            global vigor3
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                        CHOICE = input("What move do you want to use? Only type the first letter (lowercase) of the move that you want")

                Mobchoice()
            elif CHOICE == "s":
                ARAIT = weapon_damage
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            global vigor1
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            global vigor2
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            global vigor3
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                        CHOICE = input("What move do you want to use? Only type the first letter (lowercase) of the move that you want")

                Mobchoice()
            elif CHOICE == "a":
                ARAIT = weapon_damage/2
                if MOBAM == 2:
                    def arack1():
                        global vigor1
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        global vigor2
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    arack1()
                    arack2()
                if MOBAM == 3:
                    def arack1():
                        global vigor1
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        global vigor2
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    def arack3():
                        global vigor3
                        vigor3 = vigor3 - ARAIT + protection3
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                        print("Mob 3 has", vigor3, "health left")
                    arack1()
                    arack2()
                    arack3()
                if MOBAM == 4:
                    def arack1():
                        global vigor1
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        global vigor2
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    def arack3():
                            global vigor3
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                    def arack4():
                            global vigor4
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                    arack1()
                    arack2()
                    arack3()
                    arack4()
            else:
                print("Something went wrong. Please make sure you are only typing the first letter of the move in lowercase. It does not matter if the name has two words. Please type only the first letter.")
                CHOICE = input("What move do you want to use? Only type the first letter (lowercase) of the move that you want")
        def fighting3():
            global MOBAM
            global aralth
            while MOBAM > 0:
                if aralth <= 0:
                    print("You have died to the monsters. Your parents are very dissapointed in you and even though there is a revive system in this world, your parents are considering whether to use it on you.")

                elif MOBAM > 0:
                    if vigor3 <= 0:
                        if "mob3" in imagine:
                            matack3()
                            MCchoice()
                        else:
                            imagine.append("mob3")
                            MOBAM = MOBAM - 1
                            print("Congratulations!!!! You have defeated mob 3.")
                            matack3()                            
                            MCchoice()
                    elif vigor2 <= 0:
                        if "mob2" in imagine:
                            matack3()
                            MCchoice()
                        else:
                            imagine.append("mob2")
                            MOBAM = MOBAM - 1
                            print("Congratulations!!!! You have defeated mob 2.")
                            matack3()
                            MCchoice()
                    elif vigor1 <= 0:
                        if "mob1" in imagine:
                            matack3()
                            MCchoice()
                        else:
                            imagine.append("mob1")
                            MOBAM = MOBAM - 1
                            print("Congratulations!!!! You have defeated mob 1.")
                            matack3()
                            MCchoice()
                    else:
                        matack3()
                        MCchoice()
                else:
                    print("Congratulations!!!! You have defeated the room!!!! You can now proceed onto the next room.")
                    aralth = 300
        print(room_1beg)
        print("Mob 1 is a slime, Mob 2 is a slime, and Mob 3 is a slime.")
        fighting3()
        print("The mobs blocking the chest have been defeated")
        chest = input("Do you want to open the chest? Answer using yes or no. ")
        if chest == "yes":
            weapon_damage = 140
            araprotect = 20
            firepower = 290
            print("You have obtained a Basic Sword, Leather Armor, and a Hunter Bow."
            "Your damage for moves like Explosive_Shot is now 290!"
            "Your damage for moves like Slash is now 140!"
            "Your defense is now 20!")
        print(afterroom_1)

        alreadyfoughten.append("room1")
        everything_rooms_1()
weapon_damage = 140
araprotect = 20
firepower = 150
currentRoom = 3
if currentRoom == 2:
    if "room2" in alreadyfoughten:    
        everything_rooms_2()
    else: 
        imagine = []
        MOBAM = 3
        MOB1 = skeleton
        MOB2 = skeleton
        MOB3 = skeleton
        power1 = 20
        power2 = 20
        power3 = 20
        protection1 = 10
        protection2 = 10
        protection3 = 10
        vigor1 = 300
        vigor2 = 300
        vigor3 = 300
        def fighting3():
            global MOBAM
            global aralth
            while MOBAM > 0:
                if MOBAM > 0:
                    if vigor1 == 0:
                        imagine.append("mob1")
                        MOBAM = MOBAM - 1
                        print("Congratulations!!!! You have defeated mob 1.")
                        matack3()
                        MCchoice()
                    if vigor2 == 0:
                        imagine.append("mob2")
                        MOBAM = MOBAM - 1
                        print("Congratulations!!!! You have defeated mob 2.")
                        matack3()
                        MCchoice()
                    if vigor3 == 0:
                        imagine.append("mob3")
                        MOBAM = MOBAM - 1
                        print("Congratulations!!!! You have defeated mob 3.")
                        matack3()
                        MCchoice()
                    else:
                        matack3()
                        MCchoice()
                elif aralth == 0:
                        print("You have died to the monsters. Your parents are very dissapointed in you and even though there is a revive system in this world, your parents are considering whether to use it on you.")

                else:
                    print("Congratulations!!!! You have defeated the room!!!! You can now proceed onto the next room.")
                    aralth = 300
        def MCchoice():
            moveinfo()
            global vigor1
            global vigor2
            global vigor3
            CHOICE = input("What move do you want to use? Only type the first letter (lowercase) of the move that you want")
            if CHOICE == "p":
                ARAIT = int(40)
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    elif BOM == ('4'):
                        def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                        arack4()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                Mobchoice()
            elif CHOICE == "e":
                ARAIT = firepower
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    elif BOM == ('4'):
                        def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                        arack4()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                Mobchoice()
            elif CHOICE == "s":
                ARAIT = weapon_damage
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    elif BOM == ('4'):
                        def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                        arack4()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                Mobchoice()
            elif CHOICE == "a":
                ARAIT = weapon_damage/2
                if MOBAM == 2:
                    def arack1():
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    arack1()
                    arack2()
                if MOBAM == 3:
                    def arack1():
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                    arack1()
                    arack2()
                    arack3()
                if MOBAM == 4:
                    def arack1():
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                    def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                    arack1()
                    arack2()
                    arack3()
                    arack4()
            else:
                print("Something went wrong. Please make sure you are only typing the first letter of the move in lowercase. It does not matter if the name has two words. Please type only the first letter.")
                CHOICE = input("What move do you want to use? Only type the first letter (lowercase) of the move that you want")
        print(room_2beg)
        print("Mob 1 is a skeleton, Mob 2 is a skeleton, and Mob 3 is a skeleton.")
        fighting3()
        print(afterroom_2)
        alreadyfoughten.append("room2")


        everything_rooms_2()

if currentRoom == 3:
    if "room3" in alreadyfoughten:    
        everything_rooms_3()
    else: 
        imagine = []
        aralth = 300
        MOBAM = 3
        MOB1 = spider
        MOB2 = spider
        MOB3 = spider
        power1 = 30
        power2 = 30
        power3 = 30
        protection1 = 20
        protection2 = 20
        protection3 = 20
        vigor1 = 500
        vigor2 = 500
        vigor3 = 500

        def MCchoice():
            vigor1 = 500
            vigor2 = 500
            vigor3 = 500
            moveinfo()
            CHOICE = input("What move do you want to use? Only type the first letter (lowercase) of the move that you want")
            if CHOICE == "p":
                ARAIT = int(60)
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            global vigor1
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            global vigor2
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            global vigor3
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                        CHOICE = input("What move do you want to use? Only type the first letter (lowercase) of the move that you want")

                Mobchoice()
            elif CHOICE == "e":
                ARAIT = firepower
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            global vigor1
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            global vigor2
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            global vigor3
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                        CHOICE = input("What move do you want to use? Only type the first letter (lowercase) of the move that you want")

                Mobchoice()
            elif CHOICE == "s":
                ARAIT = weapon_damage
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            global vigor1
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            global vigor2
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            global vigor3
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                        CHOICE = input("What move do you want to use? Only type the first letter (lowercase) of the move that you want")

                Mobchoice()
            elif CHOICE == "a":
                ARAIT = weapon_damage/2
                if MOBAM == 2:
                    def arack1():
                        global vigor1
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        global vigor2
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    arack1()
                    arack2()
                if MOBAM == 3:
                    def arack1():
                        global vigor1
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        global vigor2
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    def arack3():
                        global vigor3
                        vigor3 = vigor3 - ARAIT + protection3
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                        print("Mob 3 has", vigor3, "health left")
                    arack1()
                    arack2()
                    arack3()
                if MOBAM == 4:
                    def arack1():
                        global vigor1
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        global vigor2
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    def arack3():
                            global vigor3
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                    def arack4():
                            global vigor4
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                    arack1()
                    arack2()
                    arack3()
                    arack4()
            else:
                print("Something went wrong. Please make sure you are only typing the first letter of the move in lowercase. It does not matter if the name has two words. Please type only the first letter.")
                CHOICE = input("What move do you want to use? Only type the first letter (lowercase) of the move that you want")
        def fighting3():
            global MOBAM
            global aralth
            while MOBAM > 0:
                if aralth <= 0:
                    print("You have died to the monsters. Your parents are very dissapointed in you and even though there is a revive system in this world, your parents are considering whether to use it on you.")

                elif MOBAM > 0:
                    if vigor3 <= 0:
                        if "mob3" in imagine:
                            matack3()
                            MCchoice()
                        else:
                            imagine.append("mob3")
                            MOBAM = MOBAM - 1
                            print("Congratulations!!!! You have defeated mob 3.")
                            matack3()                            
                            MCchoice()
                    elif vigor2 <= 0:
                        if "mob2" in imagine:
                            matack3()
                            MCchoice()
                        else:
                            imagine.append("mob2")
                            MOBAM = MOBAM - 1
                            print("Congratulations!!!! You have defeated mob 2.")
                            matack3()
                            MCchoice()
                    elif vigor1 <= 0:
                        if "mob1" in imagine:
                            matack3()
                            MCchoice()
                        else:
                            imagine.append("mob1")
                            MOBAM = MOBAM - 1
                            print("Congratulations!!!! You have defeated mob 1.")
                            matack3()
                            MCchoice()
                    else:
                        matack3()
                        MCchoice()
                else:
                    print("Congratulations!!!! You have defeated the room!!!! You can now proceed onto the next room.")
                    aralth = 300        
                    
        print("Mob 1 is a spider, Mob 2 is a spider, and Mob 3 is a spider.")
        fighting3()
        print(afterroom_3)
        alreadyfoughten.append("room3")



        everything_rooms_3()

if currentRoom == room_4:
    if "room4" in alreadyfoughten:    
        everything_room_4()
    else: 
        imagine = []
        MONAM = 3
        MOB1 = orc
        MOB2 = slime 
        MOB3 = slime
        power1 = 40
        power2 = 10
        power3 = 10
        protection1 = 30
        protection2 = 5 
        protection3 = 5
        vigor1 = 700
        vigor2 = 200
        vigor3 = 200
        def fighting3():
            global MOBAM
            global aralth
            while MOBAM > 0:
                if MOBAM > 0:
                    if vigor1 == 0:
                        imagine.append("mob1")
                        MOBAM = MOBAM - 1
                        print("Congratulations!!!! You have defeated mob 1.")
                        matack3()
                        MCchoice()
                    if vigor2 == 0:
                        imagine.append("mob2")
                        MOBAM = MOBAM - 1
                        print("Congratulations!!!! You have defeated mob 2.")
                        matack3()
                        MCchoice()
                    if vigor3 == 0:
                        imagine.append("mob3")
                        MOBAM = MOBAM - 1
                        print("Congratulations!!!! You have defeated mob 3.")
                        matack3()
                        MCchoice()
                    else:
                        matack3()
                        MCchoice()
                elif aralth == 0:
                        print("You have died to the monsters. Your parents are very dissapointed in you and even though there is a revive system in this world, your parents are considering whether to use it on you.")

                else:
                    print("Congratulations!!!! You have defeated the room!!!! You can now proceed onto the next room.")
                    aralth = 300
        def MCchoice():
            moveinfo()
            global vigor1
            global vigor2
            global vigor3
            CHOICE = input("What move do you want to use? Only type the first letter (lowercase) of the move that you want")
            if CHOICE == "p":
                ARAIT = int(40)
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    elif BOM == ('4'):
                        def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                        arack4()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                Mobchoice()
            elif CHOICE == "e":
                ARAIT = firepower
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    elif BOM == ('4'):
                        def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                        arack4()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                Mobchoice()
            elif CHOICE == "s":
                ARAIT = weapon_damage
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    elif BOM == ('4'):
                        def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                        arack4()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                Mobchoice()
            elif CHOICE == "a":
                ARAIT = weapon_damage/2
                if MOBAM == 2:
                    def arack1():
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    arack1()
                    arack2()
                if MOBAM == 3:
                    def arack1():
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                    arack1()
                    arack2()
                    arack3()
                if MOBAM == 4:
                    def arack1():
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                    def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                    arack1()
                    arack2()
                    arack3()
                    arack4()
            else:
                print("Something went wrong. Please make sure you are only typing the first letter of the move in lowercase. It does not matter if the name has two words. Please type only the first letter.")
                CHOICE = input("What move do you want to use? Only type the first letter (lowercase) of the move that you want")
        print(room_4beg)
        print("Mob 1 is a orc, Mob 2 is a slime, and Mob 3 is a slime.")
        fighting3()
        print(afterroom_4)
        alreadyfoughten.append("room4")


        everything_room_4()

if currentRoom == room_5:
    if "room5" in alreadyfoughten:    
        everything_rooms_5()
    else: 
        imagine = []
        MOBAM = 3
        MOB1 = BiG_sLIME
        MOB2 = slime 
        MOB3 = slime
        power1 = 40
        power2 = 10
        power3 = 10
        protection1 = 40
        protection2 = 5
        protection3 = 5
        vigor1 = 800
        vigor2 = 200
        vigor3 = 200
        def fighting3():
            global MOBAM
            global aralth
            while MOBAM > 0:
                if MOBAM > 0:
                    if vigor1 == 0:
                        imagine.append("mob1")
                        MOBAM = MOBAM - 1
                        print("Congratulations!!!! You have defeated mob 1.")
                        matack3()
                        MCchoice()
                    if vigor2 == 0:
                        imagine.append("mob2")
                        MOBAM = MOBAM - 1
                        print("Congratulations!!!! You have defeated mob 2.")
                        matack3()
                        MCchoice()
                    if vigor3 == 0:
                        imagine.append("mob3")
                        MOBAM = MOBAM - 1
                        print("Congratulations!!!! You have defeated mob 3.")
                        matack3()
                        MCchoice()
                    else:
                        matack3()
                        MCchoice()
                elif aralth == 0:
                        print("You have died to the monsters. Your parents are very dissapointed in you and even though there is a revive system in this world, your parents are considering whether to use it on you.")

                else:
                    print("Congratulations!!!! You have defeated the room!!!! You can now proceed onto the next room.")
                    aralth = 300
        def MCchoice():
            moveinfo()
            global vigor1
            global vigor2
            global vigor3
            CHOICE = input("What move do you want to use? Only type the first letter (lowercase) of the move that you want")
            if CHOICE == "p":
                ARAIT = int(40)
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    elif BOM == ('4'):
                        def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                        arack4()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                Mobchoice()
            elif CHOICE == "e":
                ARAIT = firepower
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    elif BOM == ('4'):
                        def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                        arack4()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                Mobchoice()
            elif CHOICE == "s":
                ARAIT = weapon_damage
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    elif BOM == ('4'):
                        def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                        arack4()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                Mobchoice()
            elif CHOICE == "a":
                ARAIT = weapon_damage/2
                if MOBAM == 2:
                    def arack1():
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    arack1()
                    arack2()
                if MOBAM == 3:
                    def arack1():
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                    arack1()
                    arack2()
                    arack3()
                if MOBAM == 4:
                    def arack1():
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                    def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                    arack1()
                    arack2()
                    arack3()
                    arack4()
            else:
                print("Something went wrong. Please make sure you are only typing the first letter of the move in lowercase. It does not matter if the name has two words. Please type only the first letter.")
                CHOICE = input("What move do you want to use? Only type the first letter (lowercase) of the move that you want")
        print(room_5beg)
        print("Mob 1 is a big slime, Mob 2 is a slime, and Mob 3 is a slime.")
        fighting3()
        print(afterroom_5)
        alreadyfoughten.append("room5")


        everything_rooms_5()

if currentRoom == room_6:
    if "room6" in alreadyfoughten:    
        everything_rooms_6()
    else: 
        imagine = []
        MOBAM = 3
        MOB1 = BiG_sLIME
        MOB2 = BiG_sLIME 
        MOB3 = slime
        power1 = 40
        power2 = 40
        power3 = 10
        protection1 = 40
        protection2 = 40
        protection3 = 5
        vigor1 = 800
        vigor2 = 800
        vigor3 = 200
        def fighting3():
            global MOBAM
            global aralth
            while MOBAM > 0:
                if MOBAM > 0:
                    if vigor1 == 0:
                        imagine.append("mob1")
                        MOBAM = MOBAM - 1
                        print("Congratulations!!!! You have defeated mob 1.")
                        matack3()
                        MCchoice()
                    if vigor2 == 0:
                        imagine.append("mob2")
                        MOBAM = MOBAM - 1
                        print("Congratulations!!!! You have defeated mob 2.")
                        matack3()
                        MCchoice()
                    if vigor3 == 0:
                        imagine.append("mob3")
                        MOBAM = MOBAM - 1
                        print("Congratulations!!!! You have defeated mob 3.")
                        matack3()
                        MCchoice()
                    else:
                        matack3()
                        MCchoice()
                elif aralth == 0:
                        print("You have died to the monsters. Your parents are very dissapointed in you and even though there is a revive system in this world, your parents are considering whether to use it on you.")

                else:
                    print("Congratulations!!!! You have defeated the room!!!! You can now proceed onto the next room.")
                    aralth = 300
        def MCchoice():
            moveinfo()
            CHOICE = input("What move do you want to use? Only type the first letter (lowercase) of the move that you want")
            if CHOICE == "p":
                ARAIT = int(40)
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    elif BOM == ('4'):
                        def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                        arack4()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                Mobchoice()
            elif CHOICE == "e":
                ARAIT = firepower
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    elif BOM == ('4'):
                        def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                        arack4()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                Mobchoice()
            elif CHOICE == "s":
                ARAIT = weapon_damage
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    elif BOM == ('4'):
                        def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                        arack4()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                Mobchoice()
            elif CHOICE == "a":
                ARAIT = weapon_damage/2
                if MOBAM == 2:
                    def arack1():
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    arack1()
                    arack2()
                if MOBAM == 3:
                    def arack1():
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                    arack1()
                    arack2()
                    arack3()
                if MOBAM == 4:
                    def arack1():
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                    def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                    arack1()
                    arack2()
                    arack3()
                    arack4()
            else:
                print("Something went wrong. Please make sure you are only typing the first letter of the move in lowercase. It does not matter if the name has two words. Please type only the first letter.")
                CHOICE = input("What move do you want to use? Only type the first letter (lowercase) of the move that you want")
        print(room_6beg)
        print("Mob 1 is a big slime, Mob 2 is a big slime, and Mob 3 is a slime.")
        fighting3()
        print(afterroom_6)
        alreadyfoughten.append("room6")
        everything_rooms_6()


if currentRoom == room_7:
    if "room7" in alreadyfoughten:    
        everything_rooms_7()
    else: 
        imagine = []
        MOBAM = 3
        MOB1 = BiG_sLIME
        MOB2 = BiG_sLIME
        MOB3 = BiG_sLIME
        power1 = 40
        power2 = 40
        power3 = 40
        protection1 = 40
        protection2 = 40
        protection3 = 40
        vigor1 = 800
        vigor2 = 800
        vigor3 = 800
        def fighting3():
            global aralth
            global MOBAM
            while MOBAM > 0:
                if MOBAM > 0:
                    if vigor1 == 0:
                        imagine.append("mob1")
                        MOBAM = MOBAM - 1
                        print("Congratulations!!!! You have defeated mob 1.")
                        matack3()
                        MCchoice()
                    if vigor2 == 0:
                        imagine.append("mob2")
                        MOBAM = MOBAM - 1
                        print("Congratulations!!!! You have defeated mob 2.")
                        matack3()
                        MCchoice()
                    if vigor3 == 0:
                        imagine.append("mob3")
                        MOBAM = MOBAM - 1
                        print("Congratulations!!!! You have defeated mob 3.")
                        matack3()
                        MCchoice()
                    else:
                        matack3()
                        MCchoice()
                elif aralth == 0:
                        print("You have died to the monsters. Your parents are very dissapointed in you and even though there is a revive system in this world, your parents are considering whether to use it on you.")

                else:
                    print("Congratulations!!!! You have defeated the room!!!! You can now proceed onto the next room.")
                    aralth = 300
        def MCchoice():
            moveinfo()
            global vigor1
            global vigor2
            global vigor3
            CHOICE = input("What move do you want to use? Only type the first letter (lowercase) of the move that you want")
            if CHOICE == "p":
                ARAIT = int(40)
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    elif BOM == ('4'):
                        def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                        arack4()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                Mobchoice()
            elif CHOICE == "e":
                ARAIT = firepower
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    elif BOM == ('4'):
                        def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                        arack4()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                Mobchoice()
            elif CHOICE == "s":
                ARAIT = weapon_damage
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    elif BOM == ('4'):
                        def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                        arack4()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                Mobchoice()
            elif CHOICE == "a":
                ARAIT = weapon_damage/2
                if MOBAM == 2:
                    def arack1():
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    arack1()
                    arack2()
                if MOBAM == 3:
                    def arack1():
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                    arack1()
                    arack2()
                    arack3()
                if MOBAM == 4:
                    def arack1():
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                    def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                    arack1()
                    arack2()
                    arack3()
                    arack4()
            else:
                print("Something went wrong. Please make sure you are only typing the first letter of the move in lowercase. It does not matter if the name has two words. Please type only the first letter.")
                CHOICE = input("What move do you want to use? Only type the first letter (lowercase) of the move that you want")
        print(room_7beg)
        print("Mob 1 is a big slime, Mob 2 is also big slime, and Mob 3 is another big slime.")
        fighting3()
        print(afterroom_7)
        alreadyfoughten.append("room7")
        everything_rooms_7()

if currentRoom == room_8:
    if "room8" in alreadyfoughten:    
        everything_rooms_8()
    else: 
        imagine = []
        MOBAM = 2
        MOB1 = skeleton
        MOB2 = orc
        power1 = 20
        power2 = 40
        protection1 = 30
        protection2 = 60
        vigor1 = 300
        vigor2 = 700
        def fighting2():
            global MOBAM
            global aralth
            if MOBAM > 0:
                if vigor1 == 0:
                    imagine.append("mob1")
                    MOBAM = MOBAM - 1
                    print("Congratulations!!!! You have defeated mob 1.")
                    matack2()
                    MCchoice()
                elif vigor2 == 0:
                    imagine.append("mob2")
                    MOBAM = MOBAM - 1
                    print("Congratulations!!!! You have defeated mob 2.")
                    matack2()
                    MCchoice()
                else:
                    matack2()
                    MCchoice()
            elif aralth == 0:
                        print("You have died to the monsters. Your parents are very dissapointed in you and even though there is a revive system in this world, your parents are considering whether to use it on you.")
            else:
                print("Congratulations!!!! You have defeated the room!!!! You can now proceed onto the next room.")
                aralth = 300
        def MCchoice():
            moveinfo()
            global vigor1
            global vigor2
            CHOICE = input("What move do you want to use? Only type the first letter (lowercase) of the move that you want")
            if CHOICE == "p":
                ARAIT = int(40)
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    elif BOM == ('4'):
                        def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                        arack4()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                Mobchoice()
            elif CHOICE == "e":
                ARAIT = firepower
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    elif BOM == ('4'):
                        def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                        arack4()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                Mobchoice()
            elif CHOICE == "s":
                ARAIT = weapon_damage
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    elif BOM == ('4'):
                        def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                        arack4()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                Mobchoice()
            elif CHOICE == "a":
                ARAIT = weapon_damage/2
                if MOBAM == 2:
                    def arack1():
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    arack1()
                    arack2()
                if MOBAM == 3:
                    def arack1():
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                    arack1()
                    arack2()
                    arack3()
                if MOBAM == 4:
                    def arack1():
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                    def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                    arack1()
                    arack2()
                    arack3()
                    arack4()
            else:
                print("Something went wrong. Please make sure you are only typing the first letter of the move in lowercase. It does not matter if the name has two words. Please type only the first letter.")
                CHOICE = input("What move do you want to use? Only type the first letter (lowercase) of the move that you want")
        print(room_8beg)
        print("Mob 1 is a armored skely, Mob 2 is also a amoured orc.")
        fighting2()
        print(afterroom_8)
        alreadyfoughten.append("room8")
        everything_rooms_8()

if currentRoom == room_9:
    if "room9" in alreadyfoughten:    
        everything_rooms_9()
    else: 
        imagine = []
        MOBAM = 4
        MOB1 = skeleton
        MOB2 = skeleton
        MOB3 = orc
        MOB4 = orc
        power1 = 20
        power2 = 20
        power3 = 40
        power4 = 40
        protection1 = 10
        protection2 = 10
        protection3 = 30
        protection4 = 30
        vigor1 = 300
        vigor2 = 300
        vigor3 = 700
        vigor4 = 700
        def fighting4():
            global MOBAM
            global aralth
            if MOBAM > 0:
                if vigor1 == 0:
                    imagine.append("mob1")
                    MOBAM = MOBAM - 1
                    print("Congratulations!!!! You have defeated mob 1.")
                    matack4()
                    MCchoice()
                elif vigor2 == 0:
                    imagine.append("mob2")
                    MOBAM = MOBAM - 1
                    print("Congratulations!!!! You have defeated mob 2.")
                    matack4()
                    MCchoice()
                elif vigor3 == 0:
                    imagine.append("mob3")
                    MOBAM = MOBAM - 1
                    print("Congratulations!!!! You have defeated mob 3.")
                    matack4()
                    MCchoice()
                elif vigor4 == 0:
                    imagine.append("mob4")
                    MOBAM = MOBAM - 1
                    print("Congratulations!!!! You have defeated mob 4.")
                    matack4()
                    MCchoice()
                else:
                    matack4()
                    MCchoice()
            elif aralth == 0:
                        print("You have died to the monsters. Your parents are very dissapointed in you and even though there is a revive system in this world, your parents are considering whether to use it on you.")

            else:
                print("Congratulations!!!! You have defeated the room!!!! You can now proceed onto the next room.")
                aralth = 300
        def MCchoice():
            moveinfo()
            global vigor1
            global vigor2
            global vigor3
            global vigor4
            CHOICE = input("What move do you want to use? Only type the first letter (lowercase) of the move that you want")
            if CHOICE == "p":
                ARAIT = int(40)
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    elif BOM == ('4'):
                        def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                        arack4()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                Mobchoice()
            elif CHOICE == "e":
                ARAIT = firepower
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    elif BOM == ('4'):
                        def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                        arack4()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                Mobchoice()
            elif CHOICE == "s":
                ARAIT = weapon_damage
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    elif BOM == ('4'):
                        def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                        arack4()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                Mobchoice()
            elif CHOICE == "a":
                ARAIT = weapon_damage/2
                if MOBAM == 2:
                    def arack1():
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    arack1()
                    arack2()
                if MOBAM == 3:
                    def arack1():
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                    arack1()
                    arack2()
                    arack3()
                if MOBAM == 4:
                    def arack1():
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                    def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                    arack1()
                    arack2()
                    arack3()
                    arack4()
            else:
                print("Something went wrong. Please make sure you are only typing the first letter of the move in lowercase. It does not matter if the name has two words. Please type only the first letter.")
                CHOICE = input("What move do you want to use? Only type the first letter (lowercase) of the move that you want")
        print(room_9beg)
        print("Mob 1 is a skeley, Mob 2 is also skeley, and Mob 3 is another orc, plus mob 4 is another orc.")
        fighting4()
        print(afterroom_9)
        alreadyfoughten.append("room9")
        everything_rooms_9()

if currentRoom == room_10:
    if "room10" in alreadyfoughten:    
        everything_rooms_10()
    elif "1234567890" in alreadyfoughten:
        print("You have gotten out of the cave sucessfully and you are no longer that big of a dissapointment to your parents. You are now D rank and is slightly better than the normal human. Congratulations!!!!")
    else: 
        imagine = []
        MOBAM = 4
        MOB1 = BiG_sLIME
        MOB2 = BiG_sLIME
        MOB3 = BiG_sLIME
        MOB4 = BiG_sLIME
        power1 = 40
        power2 = 40
        power3 = 40
        power4 = 40
        protection1 = 40
        protection2 = 40
        protection3 = 40
        protection4 = 40
        vigor1 = 800
        vigor2 = 800
        vigor3 = 800
        vigor4 = 800
        def fighting4():
            global MOBAM
            global aralth
            if MOBAM > 0:
                if vigor1 == 0:
                    imagine.append("mob1")
                    MOBAM = MOBAM - 1
                    print("Congratulations!!!! You have defeated mob 1.")
                    matack4()
                    MCchoice()
                elif vigor2 == 0:
                    imagine.append("mob2")
                    MOBAM = MOBAM - 1
                    print("Congratulations!!!! You have defeated mob 2.")
                    matack4()
                    MCchoice()
                elif vigor3 == 0:
                    imagine.append("mob3")
                    MOBAM = MOBAM - 1
                    print("Congratulations!!!! You have defeated mob 3.")
                    matack4()
                    MCchoice()
                elif vigor4 == 0:
                    imagine.append("mob4")
                    MOBAM = MOBAM - 1
                    print("Congratulations!!!! You have defeated mob 4.")
                    matack4()
                    MCchoice()
                else:
                    matack4()
                    MCchoice()
            elif aralth == 0:
                        print("You have died to the monsters. Your parents are very dissapointed in you and even though there is a revive system in this world, your parents are considering whether to use it on you.")

            else:
                print("Congratulations!!!! You have defeated the room!!!! You can now proceed onto the next room.")
                aralth = 300
        def MCchoice():
            moveinfo()
            global vigor1
            global vigor2
            global vigor3
            global vigor4
            CHOICE = input("What move do you want to use? Only type the first letter (lowercase) of the move that you want")
            if CHOICE == "p":
                ARAIT = int(40)
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    elif BOM == ('4'):
                        def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                        arack4()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                Mobchoice()
            elif CHOICE == "e":
                ARAIT = firepower
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    elif BOM == ('4'):
                        def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                        arack4()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                Mobchoice()
            elif CHOICE == "s":
                ARAIT = weapon_damage
                def Mobchoice():
                    BOM = input("List the number of the mob you want to fight against.")
                    if BOM == ('1'):
                        def arack1():
                            vigor1 = vigor1 - ARAIT + protection1
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                            print("Mob 1 has", vigor1, "health left")
                        arack1()
                    elif BOM == ('2'):
                        def arack2():
                            vigor2 = vigor2 - ARAIT + protection2
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                            print("Mob 2 has", vigor2, "health left")
                        arack2()
                    elif BOM == ('3'):
                        def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                        arack3()
                    elif BOM == ('4'):
                        def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                        arack4()
                    else: 
                        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
                Mobchoice()
            elif CHOICE == "a":
                ARAIT = weapon_damage/2
                if MOBAM == 2:
                    def arack1():
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    arack1()
                    arack2()
                if MOBAM == 3:
                    def arack1():
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                    arack1()
                    arack2()
                    arack3()
                if MOBAM == 4:
                    def arack1():
                        vigor1 = vigor1 - ARAIT + protection1
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)
                        print("Mob 1 has", vigor1, "health left")
                    def arack2():
                        vigor2 = vigor2 - ARAIT + protection2
                        print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)
                        print("Mob 2 has", vigor2, "health left")
                    def arack3():
                            vigor3 = vigor3 - ARAIT + protection3
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB3)
                            print("Mob 3 has", vigor3, "health left")
                    def arack4():
                            vigor4 = vigor4 - ARAIT + protection4
                            print(ara_ara, "has dealt", ARAIT, "damage to", MOB4)
                            print("Mob 4 has", vigor4 , "health left")
                    arack1()
                    arack2()
                    arack3()
                    arack4()
            else:
                print("Something went wrong. Please make sure you are only typing the first letter of the move in lowercase. It does not matter if the name has two words. Please type only the first letter.")
                CHOICE = input("What move do you want to use? Only type the first letter (lowercase) of the move that you want")
        print(room_10beg)
        print("Mob 1 is a big slime, Mob 2 is also big slime, and Mob 3 is another big slime, and you guessed it, mob 4 is a big slime too.")
        fighting4()
        print(afterroom_10)
        alreadyfoughten.append("room10")
        everything_rooms_10()

if currentRoom == 'CRY_PEASANTS':
    print(room_fall)
    everything_peasants()

if currentRoom == 'gambling_1':
    if "gambling1" in alreadyfoughten:
        decisions = input("Do you want to sacrifice 10 percent of your health for a chance to get better gear? Type yes or no.")
        if decisions == "yes":
            aralth = aralth - 30
            print("Your health is now", aralth)
            wish = random.randint(1, 15)
        elif decisions == "no":
            print(afterroomgambling1)
            aralth = 300
            gambling_1_everything()
        elif aralth == 0:
            print("You have died due to being too greedy. Your parents are very dissapointed in you and even though there is a revive system in this world, your parents are considering whether to use it on you.")
        else:
            print("Something went wrong, please try again.")
    elif "gambling2 " in alreadyfoughten:
        decisions = input("Do you want to sacrifice 10 percent of your health for a chance to get better gear? Type yes or no.")
        if decisions == "yes":
            aralth = aralth - 30
            print("Your health is now", aralth)
            wish = random.randint(1, 15)
        elif decisions == "no":
            print(afterroomgambling1)
            aralth = 300
            alreadyfoughten.append("gambling1")
            gambling_1_everything()
            
        elif aralth == 0:
            print("You have died due to being too greedy. Your parents are very dissapointed in you and even though there is a revive system in this world, your parents are considering whether to use it on you.")
        else:
            print("Something went wrong, please try again.")
    else:
        print("Because it is your first time coming across a wishing room, you can get one piece of gear for free. However, after this you need to sacrifice 10 percent of your health for a chance to get gear.")
        freebies = random.randint(1, 6)
        decisions = input("Do you want to sacrifice 10 percent of your health for a chance to get better gear? Type yes or no.")
        if decisions == "yes":
            aralth = aralth - 30
            print("Your health is now", aralth)
            wish = random.randint(1, 15)
        elif aralth == 0:
            print("You have died due to being too greedy. Your parents are very dissapointed in you and even though there is a revive system in this world, your parents are considering whether to use it on you.")
        elif decisions == "no":
            print(afterroomgambling1)
            aralth = 300
            alreadyfoughten.append("gambling1")
            gambling_1_everything()
        else:
            print("Something went wrong, please try again.")

if currentRoom == 'gambling_2':
    if "gambling2" in alreadyfoughten:
        decisions = input("Do you want to sacrifice 10 percent of your health for a chance to get better gear? Type yes or no.")
        if decisions == "yes":
            aralth = aralth - 30
            print("Your health is now", aralth)
            wish = random.randint(1, 15)
        elif decisions == "no":
            print(afterroomgambling2)
            aralth = 300
            gambling_2_everything()
        elif aralth == 0:
            print("You have died due to being too greedy. Your parents are very dissapointed in you and even though there is a revive system in this world, your parents are considering whether to use it on you.")
        else:
            print("Something went wrong, please try again.")
    elif "gambling1 " in alreadyfoughten:
        decisions = input("Do you want to sacrifice 10 percent of your health for a chance to get better gear? Type yes or no.")
        if decisions == "yes":
            aralth = aralth - 30
            print("Your health is now", aralth)
            wish = random.randint(1, 15)
        elif decisions == "no":
            print(afterroomgambling2)
            aralth = 300
            alreadyfoughten.append("gambling2")
            gambling_2_everything()
            
        elif aralth == 0:
            print("You have died due to being too greedy. Your parents are very dissapointed in you and even though there is a revive system in this world, your parents are considering whether to use it on you.")
        else:
            print("Something went wrong, please try again.")
            decisions = input("Do you want to sacrifice 10 percent of your health for a chance to get better gear? Type yes or no.")
    else:
        print("Because it is your first time coming across a wishing room, you can get one piece of gear for free. However, after this you need to sacrifice 10 percent of your health for a chance to get gear. It's your choice :)")
        freebies = random.randint(1, 6)
        decisions = input("Do you want to sacrifice 10 percent of your health for a chance to get better gear? Type yes or no.")
        if decisions == "yes":
            aralth = aralth - 30
            print("Your health is now", aralth)
            wish = random.randint(1, 15)
        elif decisions == "no":
            print(afterroomgambling2)
            aralth = 300
            alreadyfoughten.append("gambling2")
            gambling_2_everything()
            
        elif aralth == 0:
            print("You have died due to being too greedy. Your parents are very dissapointed in you and even though there is a revive system in this world, your parents are considering whether to use it on you.")
        else:
            print("Something went wrong, please try again.")
            decisions = input("Do you want to sacrifice 10 percent of your health for a chance to get better gear? Type yes or no.")
