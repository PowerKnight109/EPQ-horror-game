# This was the first thing I created, and was made before I decided to change genres and create a horror game. A lot of changes will need to be made to make it compatible with the rest of the code, but it provides a basic idea of how the combat would work.
import time
import random
from  parameters import v0, v, inv, items
from character_sheets import zombie

# Allows random function to be shortened
def random(range1, range2):
    import random
    temp = random.randint(range1, range2)
    return temp




def fight(enemy):
    from character_sheets import maxhealth, health, hunger, sanity, doom, atk, luck, accuracy, xp, gold
    def crit(luck):
        x = random.randint(0, 100)
        if x-luck <= 5:
            return True
        else:
            return False

    def hit(accuracy, luck):
        x = random.randint(0, 100)
        if x - luck <= accuracy:
            return True
        else:
            return False

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



    # player turn starts here
    print("a", enemy.name, "approaches!")
    turns = 0

    while enemy.health > 0 and health > 0:
        # This will count whether an action has been taken, or whether the player is exiting a menu
        turnp = True
        time.sleep(1)
        turns += 1
        print("\n\n")
        print("You have", str(health)+"/"+str(maxhealth), "health")
        time.sleep(v.Mwait)
        print("Will you:")
        time.sleep(v.Swait)
        print("A: FIGHT")
        print("B: CHECK")
        print("C: ITEM")
        action = input("D: FLEE\n")
        action = action.upper()

        if action == "A":
            print("You attack")
            time.sleep(v.Mwait)
            if hit == True:
                if crit == True:
                    print("[Vital Blow!]")
                    time.sleep(v.Mwait)
                    print("You dealt", atk + 2, "points of damage!")
                    enemy.health -= atk+2
                else:
                    print("You dealt", atk, "points of damage!")
                    enemy.health -= atk
            else:
                print("But you missed!")

        elif action == "B":
            print("CHECK")
            print("type: action")
            print("reveal the stats of the enemy, as well as some additional information about it.")
            time.sleep(v.Mwait)
            print("Do you use check?")
            time.sleep(v.Mwait)
            print("")
            print("A: Yes")
            print("B: No")
            confirm = input("")
            confirm = confirm.upper()
            if confirm == "A":
                print(enemy.name)
                time.sleep(v.Mwait)
                print("Health:", str(enemy.health) + "/" + str(enemy.maxhealth), "\nAttack:", enemy.atk, "\nAccuracy:", enemy.accuracy)
                time.sleep(3)
                print(enemy.checkdesc)
            else:
                continue
        # if special(pmoves) == True:
        #   continue

        elif action == "C":
            if items(pitem) == True:
                continue
            print(bullet)

        elif action == "D":
            print("You tried to run away")
            time.sleep(2)
            a = random.randint(speed + enemy.speed)
            if a > speed:
                print("But failed!")

            else:
                print("and did!")
                peace = True
                break


        time.sleep(v.Mwait)
        print(enemy.hitext)
        time.sleep(v.Mwait)
        if hit(enemy.accuracy, 0) == True:
            if crit(0) == True:
                print("[Vital Blow!]")
                time.sleep(v.Swait)
                print("You took", enemy.atk+2, "points of damage!")
                health -= enemy.atk+ 2
                time.sleep(v.Swait)
            else:
                print("You took", enemy.atk, "points of damage!")
                health -= enemy.atk
                time.sleep(v.Swait)
        else:
            print("But it missed!")
            time.sleep(v.Swait)

    if enemy.health <= 0 or peace == True:
        time.sleep(v.Swait)
        print("The", enemy.name, "was defeated!")
        time.sleep(v.Swait)
        print("You gained", enemy.gold, "gold from the", enemy.name + ".")
        gold += enemy.gold
        time.sleep(v.Swait)
        print("You gained", enemy.xp, "Experience Points.")
        xp = enemy.xp
        time.sleep(v.Lwait)
        print("congratulations! You won. Unfortunately, this is the end of the demo for now.")

    else:
        time.sleep(1)
        print("GAME OVER")
        time.sleep(1.5)



print(
    "-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print(
    "-------------------------------------------------------------------------------------BATTLE START!---------------------------------------------------------------------------------")
print(
    "-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
time.sleep(1)
print(fight(zombie))

# while True:
#     c =  int(input("a"))
#     d = int(input("b"))
#     print(c/d)
#