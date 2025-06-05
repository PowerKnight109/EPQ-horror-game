# This was the first thing I created, and was made before I decided to change genres and create a horror game. A lot of changes will need to be made to make it compatible with the rest of the code, but it provides a basic idea of how the combat would work.


# Allows random function to be shortened

#from character_sheets import zombie
import time
import random
from character_sheets import player
from parameters import para, misc


def fight(enemy):
    time.sleep(para.Mwait)
    enemy.health = enemy.maxhealth
    print(enemy.image)
    time.sleep(para.Lwait)
    if player.atk <1:
        player.atk = 1
    def attack(assailant, victim):
        #assailant = person attacking
        #victim = person being hit
        print(assailant.hitext)
        if random.randint(0,100) - assailant.luck + victim.luck <= assailant.accuracy:
            #check to see if attack hits
            if random.randint(0,100) - assailant.luck + victim.luck <= 5:
                #check for critical hit
                print("[Critical Blow!]")
                time.sleep(para.Mwait)
                print(assailant.name, "dealt", assailant.atk+2, "points of damage!")
                victim.health -= assailant.atk+2

            else:
                print(assailant.name, "dealt", assailant.atk, "points of damage!")
                victim.health -= assailant.atk
        else:
            print("Miss!")


    # player turn starts here
    turns = 0

    while enemy.health > 0 and player.health > 0:
        # This will count whether an action has been taken, or whether the player is exiting a menu
        turnp = True
        time.sleep(para.Swait)
        turns += 1
        if player.health > player.maxhealth:
            player.health = player.maxhealth
        if player.sanity > 100:
            player.sanity = 100
        if player.hunger > 100:
            player.hunger = 100
        print("\n\n")
        print("You have", str(player.health)+"/"+str(player.maxhealth), "health")
        time.sleep(para.Swait)
        print("Will you:")
        #time.sleep(para.Swait)
        print("A: FIGHT")
        print("B: CHECK")
        print("C: ITEM")
        action = input("D: FLEE\n")
        action = action.upper()

        if action == "A":
            print(attack(player, enemy))

        elif action == "B":
            print("CHECK")
            #print("type: action")
            print("reveal the stats of the enemy, as well as some additional information about it.")
            time.sleep(para.Mwait)
            print("Do you use check?")
            #time.sleep(para.Mwait)
            #print("")
            print("A: Yes")
            print("B: No")
            confirm = input("")
            confirm = confirm.upper()
            if confirm == "A":
                print(enemy.name)
                time.sleep(para.Mwait)
                print("Health:", str(enemy.health) + "/" + str(enemy.maxhealth), "\nAttack:", enemy.atk, "\nAccuracy:", enemy.accuracy)
                time.sleep(3)
                print(enemy.checkdesc)
                time.sleep(para.Lwait)
                print("")
            else:
                continue
        # if special(pmoves) == True:
        #   continue

        elif action == "C":
            x = player
            from invmenu import inventory
            inventory()
            if player == x:
                continue

        elif action == "D":
            print("You tried to run away")
            time.sleep(2)
            a = random.randint(0, player.speed+ enemy.speed) - player.luck
            if a > player.speed:
                print("But failed!")

            else:
                print("and did!")
                time.sleep(para.Swait)
                print("[Distance -1]")
                print("[Hunger -" + str(para.smallchange) + "]")
                player.hunger -= para.smallchange
                misc.distance -= 1
                peace = True
                break


        time.sleep(para.Mwait)
        if enemy.health > 0:
            attack(enemy, player)


    if enemy.health <= 0:
        time.sleep(para.Swait)
        print(enemy.losetext)
        time.sleep(para.Swait)
        print("You gained", enemy.gold, "gold from the", enemy.name + ".")
        player.gold += enemy.gold
        time.sleep(para.Swait)
        print("You gained", enemy.xp, "Experience Points.")
        player.xp += enemy.xp
        while player.xp >= player.mxp:
            print("You feel yourself becoming stronger!")
            time.sleep(para.Mwait)
            print("[Max Health +1]")
            print("[Health +3]")
            print("[Attack +1]")
            print("[Luck +2]")

            player.atk += 1
            player.maxhealth += 1
            player.health += para.smallhprestore
            player.luck += 1
            player.xp -= player.mxp
            player.mxp += 25
        return True




    elif player.health <=0:
        time.sleep(1)
        print(enemy.wintext)
        time.sleep(1.5)
        print("GAME OVER")



# print(
#     "-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
# print(
#     "-------------------------------------------------------------------------------------BATTLE START!---------------------------------------------------------------------------------")
# print(
#     "-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
time.sleep(para.Swait)
#print(fight(zombie))

# while True:
#     c =  int(input("a"))
#     d = int(input("b"))
#     print(c/d)
##