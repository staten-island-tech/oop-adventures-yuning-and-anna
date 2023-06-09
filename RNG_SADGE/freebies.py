import random
from Skills.movves import *

Item = []

if freebies == 1:
    if "katana" in Item:
        freebies = random.randint(2, 6)
    elif weapon_damage > 84:
        freebies = random.randint(2, 6)
    else:
        weapon_damage = 85
        Item.append("katana")
        print("Congrats! You have gotten a Katana! Your damage for moves like Slash is now 85!")
        
if freebies == 2:
    if "crossbow" in Item:
        freebies = random.randint(1, 6)
    elif firepower > 199:
        freebies = random.randint(1, 6)
    else:
        firepower = 200
        Item.append("crossbow")
        print("Congrats! You have gotten a Crossbow! Your damage for moves like Explosive_Shot is now 200!")

if freebies == 3:
    if "bonearmor" in Item:
        freebies = random.randint(1, 6)
    elif araprotect > 19:
        freebies = random.randint(1, 6)
    else:
        araprotect = 20
        Item.append("bonearmor")
        print("Congrats! You have gotten a piece of Bone Armor! Your defense is now 20!")

if freebies == 4:
    if "valkyrie" in Item:
        freebies = random.randint(1, 6)
    elif weapon_damage > 109:
        freebies = random.randint(1, 6)
    else:
        weapon_damage = 110
        Item.append("valkyrie")
        print("Congrats! You have gotten a Valkyrie! Your damage for moves like Slash is now 110!")

if freebies == 5:
    if "piercerofshadows" in Item:
        freebies = random.randint(1, 6)
    elif firepower > 249:
        freebies = random.randint(1, 6)
    else:
        firepower = 250
        Item.append("piercerofshadows")
        print("Congrats! You have gotten a Piercer of Shadows! Your damage for moves like Explosive_Shot is now 250!")

if freebies == 6:
    if "mithrilarmor" in Item:
        freebies = random.randint(1, 6)
    elif araprotect > 29:
        freebies = random.randint(1, 6)
    else:
        araprotect = 30
        Item.append("mithrilarmor")
        print("Congrats! You have gotten a piece of Mithril Armor! Your defense is now 30!")



        

