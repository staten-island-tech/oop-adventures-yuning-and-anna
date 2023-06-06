from Roms.introduction_to_room import *

from Roms.roms import * 

from ChARActer.chARActer import *

from MOBS.mobsC import *

from Skills.movves import *

from Skills.movves import *

def Mattack1():
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

def Mattack4():
    HIT = MOB4.strength - ara_ara.defense
    ara_ara.health = ara_ara.health - HIT
    print(MOB4, "has dealt", HIT, "damage to", ara_ara)
    return ara_ara.health

def arack1():
    MOB1.vitality = MOB1.vitality - ARAIT + MOB1.thick_skin
    print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)

def arack2():
    MOB2.vitality = MOB2.vitality - ARAIT + MOB2.thick_skin
    print(ara_ara, "has dealt", ARAIT, "damage to", MOB2)

def arack3():
    MOB3.vitality = MOB3.vitality - ARAIT + MOB3.thick_skin
    print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)

def arack4():
    MOB4.vitality = MOB4.vitality - ARAIT + MOB4.thick_skin
    print(ara_ara, "has dealt", ARAIT, "damage to", MOB1)

def Mobchoice():
    BOM = input("List the number of the mob you want to fight against.")
    if BOM = 1:
        def arack1()
    

 
def moveinfo():
    print("In this game, there are 5 different moves that you can use"
    "They are punch, slash, explosive shot, armor pierce, and air cutter."
    "Punch does 40 damage if the enemy has no defense and you don't need any weapons"
    "Slash does the damage of your weapon, so if you don't have a weapon, it does no damage."
    "Explosive shot does the damage of your bow, so if you don't have a bow, it does no damage. Additionally, this move takes two rounds, so plan accordingly."
    "Lastly, Air Cutter is an AOE type of move, so it attacks all enemies. It does half the damage of your weapon, so if you don't have a weapon, it does no damage.")

def MCchoice():
    moveinfo()
    CHOICE = input("What move do you want to use? Only type the first letter (lowercase) of the move that you want")
    if CHOICE == p:
        ARAIT = 40
    if CHOICE == e:
        ARAIT == firepower
    if CHOICE == s:
        ARAIT == 




        


    
     

