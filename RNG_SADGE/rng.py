import random
from Skills.movves import *
from ChARActer.chARActer import *
from RNG_SADGE.freebies import Item

if wish == 1:
    if "katana" in Item:
        wish = random.randint(2, 15)
    elif weapon_damage > 84:
        wish = random.randint(2, 15)
    else:
        weapon_damage = 85
        Item.append("katana")
        print("Congrats! You have gotten a Katana! Your damage for moves like Slash is now 85!")

        
if wish == 2:
    if "crossbow" in Item:
        wish = random.randint(1, 15)
    elif firepower > 199:
        wish = random.randint(1, 15)
    else:
        firepower = 200
        Item.append("crossbow")
        print("Congrats! You have gotten a Crossbow! Your damage for moves like Explosive_Shot is now 200!")

if wish == 3:
    if "bonearmor" in Item:
        wish = random.randint(1, 15)
    elif defense > 19:
        wish = random.randint(1, 15)
    else:
        defense = 20
        Item.append("bonearmor")
        print("Congrats! You have gotten a piece of Bone Armor! Your defense is now 20!")

if wish == 4:
    if "valkyrie" in Item:
        wish = random.randint(1, 15)
    elif weapon_damage > 109:
        wish = random.randint(1, 15)
    else:
        weapon_damage = 110
        Item.append("valkyrie")
        print("Congrats! You have gotten a Valkyrie! Your damage for moves like Slash is now 110!")

if wish == 5:
    if "piercerofshadows" in Item:
        wish = random.randint(1, 15)
    elif firepower > 249:
        wish = random.randint(1, 15)
    else:
        firepower = 250
        Item.append("piercerofshadows")
        print("Congrats! You have gotten a Piercer of Shadows! Your damage for moves like Explosive_Shot is now 250!")

if wish == 6:
    if "mithrilarmor" in Item:
        wish = random.randint(1, 15)
    elif defense > 29:
        wish = random.randint(1, 15)
    else:
        defense = 30
        Item.append("mithrilarmor")
        print("Congrats! You have gotten a piece of Mithril Armor! Your defense is now 30!")

if wish == 7:
    if "katana" in Item:
        wish = random.randint(1, 15)
    elif weapon_damage > 84:
        wish = random.randint(1, 15)
    else:
        weapon_damage = 85
        Item.append("katana")
        print("Congrats! You have gotten a Katana! Your damage for moves like Slash is now 85!")
     
if wish == 8:
    if "crossbow" in Item:
        wish = random.randint(1, 15)
    elif firepower > 199:
        wish = random.randint(1, 15)
    else:
        firepower = 200
        Item.append("crossbow")
        print("Congrats! You have gotten a Crossbow! Your damage for moves like Explosive_Shot is now 200!")

if wish == 9:
    if "bonearmor" in Item:
        wish = random.randint(1, 15)
    elif defense > 19:
        wish = random.randint(1, 15)
    else:
        defense = 20
        Item.append("bonearmor")
        print("Congrats! You have gotten a piece of Bone Armor! Your defense is now 20!")

if wish == 10:
    aralth = aralth - 30
    print("You have invocked bad luck. MUHAHAHAHAHAH. Your health has decreased by 10%")

if wish == 11:
    print("You have gotten nothing! You might be sad but it's better than losing something, right? So be happy that you are not dead right now.")

if wish == 12:
    print("You have gotten nothing! You might be sad but it's better than losing something, right? So be happy that you are not dead right now.")

if wish == 13:
    print("You have gotten nothing! You might be sad but it's better than losing something, right? So be happy that you are not dead right now.")

if wish == 14:
    print("You have gotten nothing! You might be sad but it's better than losing something, right? So be happy that you are not dead right now.")

if wish == 15:
    print("You have gotten nothing! You might be sad but it's better than losing something, right? So be happy that you are not dead right now.")




