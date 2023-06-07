from Roms.introduction_to_room import *

from Roms.roms import * 

from ChARActer.chARActer import *

from MOBS.mobsC import *

from Skills.movves import *

from Skills.movves import *

def starting():
    beginning = input("Type start when are ready to begin ")
    if beginning == "start":
        print(intro_room_beginning)
    else:
        print("Try again when you are ready")
        beginning = input("Type start when are ready to begin ")
ARAIT = 0
def MCchoice():
    moveinfo()
    CHOICE = input("What move do you want to use? Only type the first letter (lowercase) of the move that you want")
    if CHOICE == p:
        ARAIT = 40
        Mobchoice()
    elif CHOICE == e:
        ARAIT = firepower
        Mobchoice()
    elif CHOICE == s:
        ARAIT = weapon_damage
        Mobchoice()
    elif CHOICE == a:
        ARAIT = weapon_damage/2
        if MOBAM == 2:
            arack1()
            arack2()
        if MOBAM == 3:
            arack1()
            arack2()
            arack3()
        if MOBAM == 4:
            arack1()
            arack2()
            arack3()
            arack4()
    else:
        print("Something went wrong. Please make sure you are only typing the first letter of the move in lowercase. It does not matter if the name has two words. Please type only the first letter.")
        CHOICE = input("What move do you want to use? Only type the first letter (lowercase) of the move that you want")

def Mattack1():
    HIT = power1 - ara_ara.defense
    aralth = aralth - HIT
    print(MOB1, "has dealt", HIT, "damage to", ara_ara)
    print(ara_ara, "has", aralth,"left")

def Mattack2():
    HIT = power2 - ara_ara.defense
    aralth = aralth - HIT
    print(MOB2, "has dealt", HIT, "damage to", ara_ara)
    print(ara_ara, "has", aralth,"left")

def Mattack3():
    HIT = power3 - ara_ara.defense
    aralth = aralth - HIT
    print(MOB3, "has dealt", HIT, "damage to", ara_ara)
    print(ara_ara, "has", aralth,"left")

def Mattack4():
    HIT = power4 - ara_ara.defense
    aralth = aralth - HIT
    print(MOB4, "has dealt", HIT, "damage to", ara_ara)
    print(ara_ara, "has", aralth,"left")

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

def Mobchoice():
    BOM = input("List the number of the mob you want to fight against.")
    if BOM == 1:
        arack1()
    elif BOM == 2:
        arack2()
    elif BOM == 3:
        arack3()
    elif BOM == 4:
        arack4()
    else: 
        print("Make sure that you are typing in the correct number of the corresponding mob that you want to attack.")
    

 
def moveinfo():
    print("In this game, there are 5 different moves that you can use"
    "They are punch, slash, explosive shot, armor pierce, and air cutter."
    "Punch does 40 damage if the enemy has no defense and you don't need any weapons"
    "Slash does the damage of your weapon, so if you don't have a weapon, it does no damage."
    "Explosive shot does the damage of your bow, so if you don't have a bow, it does no damage. Additionally, this move takes two rounds, so plan accordingly."
    "Lastly, Air Cutter is an AOE type of move, so it attacks all enemies. It does half the damage of your weapon, so if you don't have a weapon, it does no damage.")

