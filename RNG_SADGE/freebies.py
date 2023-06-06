import random
weapon_damage = 0
Item = []


freebies = random.randint(1, 1)

if freebies == 1:
    if "katana" in Item:
        freebies = random.randint(2,3)
    elif weapon_damage > 84:
        freebies = random.randint(2,2)
        print(freebies)
    else:
        weapon_damage = 85
        Item.append("katana")
        print("Congrats! You have gotten a Katana! Your damage for moves like Slash is now 85!")
        
if freebies == 2:
    if "crossbow" in Item:
        freebies = random.randint(1, 3)
    elif firepower > 199:
        freebies = random.randint(1, 3)
    else:
        firepower = 200
        Item.append("crossbow")
        print("Congrats! You have gotten a Crossbow! Your damage for moves like Explosive_Shot is now 200!")

if freebies == 3:
    if "bonearmor" in Item:
        wish = random.randint(1, 3)
    elif defense > 19:
        wish = random.randint(1, 3)
    else:
        defense = 20
        Item.append("bonearmor")
        print("Congrats! You have gotten a piece of Bone Armor! Your defense is now 20!")








        

