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
        print(weapon_damage)
        Item.append("katana")
        print(Item)
        

