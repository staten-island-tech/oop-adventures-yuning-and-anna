import random
from Skills.movves import *
from ChARActer.chARActer import *
Item = []

freebies = random.randint(0, 1)
print(freebies)
if freebies == 1:
    if "katana" in Item:
        freebies = random.randint(0, 6)
    elif weapon_damage > 85:
        print("You got a Katana! Yay! But this does less damage than you current weapon so it would not be applied! So sorry! Good luck on the journey!!!!")
    else:
        weapon_damage = 85
        Item.append("katana")
        print(Item)
        

