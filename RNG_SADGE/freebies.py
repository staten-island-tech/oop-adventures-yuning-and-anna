import random
weapon_damage = 0
Item = []


freebies = random.randint(1, 1)
print(freebies)
if freebies == 1:
    if "katana" in Item:
        freebies = random.randint(2,2)
    elif weapon_damage > 85:
        freebies = random.randint(2,2)
        print(freebies)
    else:
        weapon_damage = 85
        Item.append("katana")
        print("Congrats! You have gotten a Katana! Your damage for moves like Slash is now 85!")
        print(weapon_damage)
        print(Item)
        
if freebies == 2:
    if "dsada" in Item:
        freebies = random.randint(0, 6)
    elif weapon_damage > 890:
        freebies = random.randint(0, 6)
        print(freebies)
    else:
        weapon_damage = 85
        Item.append("dsadsa")
        print("Congrats! You have gotten a dsadsa! Your damage for moves like Slash is now 85!")
        print(weapon_damage)
        

