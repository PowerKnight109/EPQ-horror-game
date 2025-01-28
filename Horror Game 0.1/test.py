import time
import random
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)
steps = 2
sanity = 50

class stats:
    def __init__(self, maxhealth, health, hunger, sanity, doom, atk, luck, accuracy, xp, gold):
        self.maxhealth = maxhealth
        self.health = health
        self.hunger = hunger
        self.sanity = sanity
        self.doom = doom
        self.atk = atk
        self.luck = luck
        self.accuracy = accuracy
        self.xp = xp
        self.gold = gold

player = stats(10, 10, 100, 100, 0, 1, 0, 80, 0, 0)
maxhealth = player.maxhealth
health = player.health
hunger = player.hunger
sanity = player.sanity
doom = player.doom
atk = player.atk
luck = player.luck
accuracy = player.accuracy
xp = player.xp
gold = player.gold



# function, type in variable name and


#Values are the stat you want changed, the amount it changes by, and the amount it changes by under DOOM
def statchange(targetstat, change, doomchange):
    global statdiff
    if player.doom < 50:
        targetstat += change
        statdiff = change
    elif doom >= 50:
        targetstat += doomchange
        statdiff = doomchange
    return targetstat



health = statchange(health, -1, -2)
print(health)
print(statdiff)

#player = maxhealth, health, hunger, sanity, atk, luck, xp, gold
#maxhealth = 0
#health = 1
#hunger = 2
#sanity = 3
#atk = 4
#luck = 5
#xp = 6
# gold = 7
player = [10, 10, 100, 100, 1, 0, 0, 0]
