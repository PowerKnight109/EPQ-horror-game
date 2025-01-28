#This was the first thing I created, and was made before I decided to change genres and create a horror game. A lot of changes will need to be made to make it compatible with the rest of the code, but it provides a basic idea of how the combat would work.



import time
"player = [type, maxhealth, health, damage, accuracy, speed, xp]" "moves"
#pmoves = [100,"check","minor illusion", "minor healing", "cure", "illusion", "ray of light", "bless", "kamakazi", "mischief", "ULTIMATE- Heaven's Gate"] 
pitem = ["Gun", "Health Potion"]
hpot = "3"
#mpot = "3"
bullet = "1"
gold = "0"
"70 health"
playerstat = ["neutral", 100, 70, 10, 80, 5, 0] 
"pmoves"
"metastat = maxhealth, health, bullet, hpot, gold, xp, placement"    "mpot"
#This will be where variables outside of battle will be stored.
metastat = open("gameinfo.txt", "w")
metastat.write(str(playerstat[1])+"\n"+str(playerstat[2])+"\n"+bullet+"\n"+hpot+"\n"+gold + "\n" + str(playerstat[6])+"\n"+str("1"))
metastat.close()
# print("player =", player)
print("")
#Allows random function to be shortened
def random(range1, range2):
    import random
    temp = random.randint(range1, range2)
    return temp
#Enemy stats
"enemy = [name, weakness, resistance, maxhealth, health, damage, accuracy, speed, drops, xp]"
"moves"
zweak = ["light", "fire"]
zresist = ["poison", "dark"]
#zmoves = [100, "bite", "kafrizzle", "curse", "corpse rot", "resiliance", "blind", "infestation"]
"10,15"
zmhealth = random(50,150)
zombiestat = ["zombie",zweak, zresist, zmhealth, zmhealth, random(5,20), random(70, 100), random(0,10), random(0,50), random(0, 100)]
"zmoves"
# print("zombie =", zombie)
# time.sleep(2)

def replace(place, value):
    lines = open("gameinfo.txt", 'r').readlines()
    lines[place] = str(value)+"\n"
    out = open("gameinfo.txt", 'w')
    out.writelines(lines)
    out.close()

        
def fight(enemy, player):
    middle = ["   O", "  <O>", " <<O>>", "<<<O>>>", "<<< >>>", "<<   >>", "<     >"]
    batstat = open("gameinfo.txt", "r")
    batstat.readline()
    batstat.readline()
    mxbull = int(batstat.readline())
    mxhpot = int(batstat.readline())
    batstat.close()
    def crit(accuracy):
        accuracyv = [70, 75, 80, 85, 90, 95, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
        critv = [1, 3, 5, 7, 10, 12, 15, 20, 25, 35, 40, 50, 60, 70, 80, 90, 100]
        temp = 0
        for i in range(len(accuracyv)):
            if accuracy >= accuracyv[i]:
                temp = critv[i]
        return int(temp)
#     def special(char):
#         while True:
#             back = False
#             print("You have", pmoves[0], "mana")
#             time.sleep(1)
#             for m in range(1,len(pmoves)):
#                 print((chr(m+64))+":", pmoves[m])
#             print(chr(len(pmoves)+64)+":", "back")
#             charselect = input("")
#             if ord(charselect.upper())-64 == len(pmoves):
#                 back = True
#                 return(back)
#                 break
        
#             else:
#                 reverse = pmoves[ord(charselect.upper())-64]
#                 print(reverse)
                
#                 if reverse == "check":
#                     print("CHECK")
#                     print("type: action")
#                     print("reveal the stats of the enemy")
#                     time.sleep(1)
#                     print("Do you use check?")
#                     time.sleep(1)
#                     print("")
#                     print("A: Yes")
#                     print("B: No")
#                     confirm = input("")
#                     confirm = confirm.upper()
#                     if confirm == "A":
#                         print(enemy[0])
#                         print("Health:", str(enemy[4]) + "/" + str(enemy[3]))
#                         print("Attack:", enemy[5])
#                         print("Speed:", enemy[7])
#                         time.sleep(3)
#                         break
                        
#                 elif reverse == "minor illusion":
#                     print("Minor Illusion")
#                     print("type: psychic magic")
#                     print("mana cost: 10")
#                     print("You attempt to utterly dumfound the enemy with a card trick, confusing them")
#                     print("Do you attempt to cast minor illusion?")
#                     time.sleep(1)
#                     print("")
#                     print("A: Yes")
#                     print("B: No")
#                     confirm = input("")
#                     if confirm == "A":
#                         print("You cast minor illusion")
                        #i
    def items(inv):
        gunanim = ["¬"]
        while True:
            back = False
            print("Your items are:")
            for i in range(len(pitem)):
                print((chr(i+65))+":", pitem[i])
            print(chr(len(pitem)+65)+":", "back")
            charselect = input("")
            if ord(charselect.upper())-65 == len(pitem):
                back = True
                return(back)
                break
            else:
                reverse = pitem[ord(charselect.upper())-65]
                print(reverse)
                if reverse == "Gun":
                    batstat = open("gameinfo.txt", "r")
                    batstat.readline()
                    batstat.readline()
                    shots = int(batstat.readline())
                    batstat.close()
                    print("You have", shots, "bullets")
                    time.sleep(1)
                    print("Fire the gun?")
                    time.sleep(1)
                    print("A: Yes")
                    print("B: No")
                    fire = input("")
                    if fire.upper() == "A" and shots > 0:
                        print("You fired the gun")
                        time.sleep(1)
                        for x in range(136):
                            finanim = ""
                            for y in range(len(gunanim)):
                                finanim += gunanim[y]
                            print(finanim)
                            gunanim.insert(0, "-")
                        time.sleep(1)
                        print("The", enemy[0], "took 100 damage!")
                        enemy[4] -= 100
                        shots -= 1
                        replace(2, shots)
                        break
                    elif fire.upper() == "A" and shots <= 0:
                        print("You're out of bullets!")
                    #potion
                elif reverse == "Health Potion":
                    batstat = open("gameinfo.txt", "r")
                    batstat.readline()
                    batstat.readline()
                    batstat.readline()
                    flasks = int(batstat.readline())
                    batstat.close()
                    print("You have", flasks, "health potions")
                    time.sleep(1)
                    print("Consume a health potion?")
                    time.sleep(1)
                    print("A: Yes")
                    print("B: No")
                    consume = input("")
                    if consume.upper() == "A" and flasks > 0:
                        print("You consumed a health potion")
                        time.sleep(1)
                        print("")
                        print("               +++++++")
                        print("               +++++++")
                        print("               +++++++")
                        print("        +++++++++++++++++++++")
                        print("        +++++++++++++++++++++")
                        print("        +++++++++++++++++++++")
                        print("               +++++++")
                        print("               +++++++")       
                        print("               +++++++")
                        print("")
                        time.sleep(1)
                        oldh = player[2]
                        player[2] += 30
                        if player[2] > player[1]:
                            player[2] = player[1]
                        print("You recovered", player[2] - oldh, "health")
                        flasks -= 1
                        replace(1, player[2])
                        replace(3, flasks)
                        break
                    elif consume.upper() == "A" and flasks <= 0:
                        print("You're out of health potions!")
                    else:
                        turnp = False
                        break

        
    #player turn starts here
    print("a", enemy[0], "blocks your path!")
    turns = 0
    peace = False
#     res = False
    #while (enemy[4] > 0 or res == True) and player[2] > 0:
    while enemy[4] > 0 and player[2] > 0:
#         if enemy[4] <= 0 and res == True:
#             print("The", enemy[0], "survived thanks to resiliance!")
#             enemy[4] = 1
#             res = False
        #This will count whether an action has been taken, or whether the player is exiting a menu 
        turnp = True
        time.sleep(1)
        turns += 1
        print("")
        print("")
        print("")
        print("Will you:")
        print("A: FIGHT")
        print("B: CHECK")
        print("C: ITEM")
        print("D: FLEE ")
        print("")
        print("You have", player[2], "health")
        action = input("")
        action = action.upper()
        
        if enemy[7] > player[5] and enemy[4] > 0 and Turnp == True:
            print(enemy[0], "attacks!")
            time.sleep(1.5)
            if enemy[6] >= random(0,100):
                for y in range(20):
                    print("")
                for x in range(len(middle)):
                    for i in range(5):
                        print("   ^")
                        print(middle[x])
                        print("   v")
                for z in range(20):
                    print("")
                if crit(enemy[6]) > random(0,100):
                    print("CRITICAL HIT!")
                    time.sleep(1)
                    print("Deals", enemy[5]*2, "points of damage!")
                    player[2] -= enemy[5]*2
                else:
                    print("Deals", enemy[5], "points of damage!")
                    player[2] -= enemy[5]
            else:
                print("But it missed!")
        else:
                turnp = True
                
        if action == "A":
            print("You attack")
            time.sleep(1.5)
            if player[4] >= random(0,100):
                for y in range(20):
                    print("")
                for x in range(len(middle)):
                    for i in range(5):
                        print("   ^")
                        print(middle[x])
                        print("   v")
                for z in range(20):
                    print("")
                time.sleep(0.5)
                if crit(player[4]) >= random(0,100):
                    print("CRITICAL HIT!")
                    time.sleep(1)
                    print("You dealt", player[3]*2, "points of damage!")
                    enemy[4] -= player[3]*2
                else:
                    print("You dealt", player[3], "points of damage!")
                    enemy[4] -= player[3]
            else:
                print("But you missed!")
        
        elif action == "B":
            print("CHECK")
            print("type: action")
            print("reveal the stats of the enemy")
            time.sleep(1)
            print("Do you use check?")
            time.sleep(1)
            print("")
            print("A: Yes")
            print("B: No")
            confirm = input("")
            confirm = confirm.upper()
            if confirm == "A":
                print(enemy[0])
                print("Health:", str(enemy[4]) + "/" + str(enemy[3]))
                print("Attack:", enemy[5])
                print("Speed:", enemy[7])
                print("Accuracy:", enemy[6])
                time.sleep(3)
            else:
                continue
           #if special(pmoves) == True:
             #   continue
        
        elif action == "C":
            if items(pitem) == True:
                continue
            print(bullet)
        
        elif action == "D":
            print("You tried to run away")
            time.sleep(2)
            a = 100*(player[5]/(player[5]+enemy[7]))
            if a < random(0,100):
                print("But failed!")
                
            else:
                print("and did!")
                peace = True
                break

                
        if enemy[7] <= player[5] and enemy[4] > 0:
            time.sleep(1)
            print(enemy[0], "attacks!")
            time.sleep(1.5)
            if enemy[6] >= random(0,100):
                for y in range(20):
                    print("")
                for x in range(len(middle)):
                    for i in range(5):
                        print("   ^")
                        print(middle[x])
                        print("   v")
                for z in range(20):
                    print("")
                if crit(enemy[6])>= random(0,100):
                    print("CRITICAL HIT!")
                    time.sleep(1)
                    print("Deals", enemy[5]*2, "points of damage!")
                    player[2] -= enemy[5]*2
                    time.sleep(1)
                else:
                    print("Deals", enemy[5], "points of damage!")
                    player[2] -= enemy[5]
                    time.sleep(1)
            else:
                print("But it missed!")
                time.sleep(1)

    if enemy[4] <= 0 or peace == True:
        time.sleep(1)
        print("The", enemy[0], "was defeated!")
        replace(1, player[2])
        time.sleep(1)
        print("You gained", enemy[8], "gold from the", enemy[0]+".")
        replace(4,enemy[8])
        time.sleep(1)
        print("You gained", enemy[9], "Experience Points.")
        replace(5, enemy[9])
        time.sleep(1.5)
        print("congratulations! You won. Unfortunately, this is the end of the demo for now.")
        
    else:
        time.sleep(1)
        print("GAME OVER")
        time.sleep(1.5)
        replace(2, mxbull)
        replace(3, mxhpot)
        replace(6, 2)
        time.sleep(2)

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------BATTLE START!---------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
time.sleep(1)
print(fight(zombiestat, playerstat))

# while True:
#     c =  int(input("a"))
#     d = int(input("b"))
#     print(c/d)
#     
