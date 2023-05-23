import random
from Skills.movves import *
from ChARActer.chARActer import *
Item = []

freebies = random.randint(0, 1)
print(freebies)
if freebies == 1:
    if "katana" in Item:
        freebies = random.randint(0, 6)
    else:
        weapon_damage = 85
        Item.append("katana")
        print("Congrats! You have gotten a Katana! Your damage for moves like Slash is now 85!")
if freebies == 2:
    if "katana" in Item:
        freebies = random.randint(0, 6)
    else:
        weapon_damage = 85
        Item.append("katana")
        print("Congrats! You have gotten a Katana! Your damage for moves like Slash is now 85!")
        

