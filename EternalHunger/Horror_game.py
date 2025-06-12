import time
import random
from parameters import para, misc, stalking
from invmenu import inventory, words
from character_sheets import player, enemies
from encounters import encounterpick, eventable
from ending import ZathKopchyla

def intro():
    print("ETERNAL HUNGER")
    time.sleep(para.Mwait)
    print("You wake up")
    time.sleep(para.Mwait)
    print("You sit in a dingy, rot-infested room")
    time.sleep(para.Mwait)
    print("Corpses and strange runes are strewn about")
    time.sleep(para.Mwait)
    # print("You find a dagger on the ground next to a note, which reads 'ZATH-KOPCHYLA CANNOT BE SUMMONED'")
    # time.sleep(para.Mwait)
    print("You pick up a dagger from one of the corpses and step outside")
    time.sleep(para.Mwait)
    input("Press enter to take a step forward\n")

    #Loop ends when the player reaches 50m, or when health, hunger or stamina reach 0.
     #Will have loop end at max doom later


def gameloop():
    #from encounters import eventable
    # Values are the stat you want changed, the amount it changes by, and the amount it changes by under DOOM
    validevents = []

    # Function used when an event has a random outcome
    def skillcheck(luck, minnumber):
        # minnumber is the percentage chance of success. 75% = (minnumber = 75)
        if (random.randint(1, 100) - luck) <= minnumber:
            return True
        else:
            return False
    last = "geeblock"
    while misc.distance < 50 and player.health > 0 and player.hunger >= 0 and player.sanity > 0:
        time.sleep(para.Swait)
        precount = player.inv["charm"]
        if player.health > player.maxhealth:
            player.health = player.maxhealth
        if player.sanity > 100:
            player.sanity = 100
        if player.hunger > 100:
            player.hunger = 100
        print("\n\n\n\n\nYou have traveled", misc.distance, "meters")
        print("Health:", str(player.health) + "/" + str(player.maxhealth))
        print("Hunger:", player.hunger)
        print("Sanity:", player.sanity)
        print("press enter to step forward")
        print("enter 'I' to access inventory")
        proceed = input().lower()

        if proceed == "i":
            inventory()

        elif proceed == "the cake is a lie" or proceed == "thecakeisalie" or proceed == "d":
            print("[DEBUG MODE ACTIVATED]")
            debug = input("A: Activate Godmode\nB: Activate Turbo\nC: Event Gallery\nD: Image Gallery\nE: Set custom values\n").lower()
            if debug == "a":
                print("[GODMODE ACTIVATED]")
                player.atk = 100
                player.maxhealth = 100
                player.health = 100
                player.luck = 100
                player.accuracy = 100
                player.gold = 999
                for i in range(len(words)):
                    player.inv[words[i]] += 99

            elif debug == "b":
                print("[TURBO MODE ACTIVATED]")
                para.Mwait = 0
                para.Swait = 0
                para.Lwait = 0

            elif debug == "c":
                def look(e):
                    return e.diff
                eventable.sort(key=look)
                for i in range(len(eventable)):
                    print(str(i)+":", eventable[i].name)
                choose = int(input("Please enter the corresponding number of the event that you'd like to view\n"))
                eventable[choose].text()

            elif debug == "d":
                for i in range(len(enemies)):
                    print(enemies[i].name+"\n"+enemies[i].image+"\n\n\n")

            elif debug == "e":
                while True:
                    x = input("A: Max Health\nB: Health\nC: Hunger\nD: Sanity\nE: Attack\nF: Luck\nG: Speed\nH: Accuracy\nI: XP\nJ: Gold\nK: Meat\nL: Pills\nM: Bandages\nN: Charm\nO: Steroids\nP: Distance\nQ: Difficulty\nR: Bullets\nS: Gun\nT: Go Back\nWhich value would you like to adjust?\n").lower()
                    #Yes, I know the code here is horrible, but it
                    if x == "t":
                        break
                    else:
                        number = int(input("What number would you like to set the value to?\n"))
                        if x == "a":
                            player.maxhealth = number
                        elif x == "b":
                            player.health = number
                        elif x == "c":
                            player.hunger = number
                        elif x == "d":
                           player.sanity  = number
                        elif x == "e":
                            player.atk = number
                        elif x == "f":
                            player.luck = number
                        elif x == "g":
                            player.speed = number
                        elif x == "h":
                            player.accuracy = number
                        elif x == "i":
                            player.xp = number
                        elif x == "j":
                            player.gold = number
                        elif x == "k":
                            player.inv["meat"] = number
                        elif x == "l":
                            player.inv["pills"] = number
                        elif x == "m":
                            player.inv["bandages"] = number
                        elif x == "n":
                            player.player.inv["charm"] = number
                        elif x == "o":
                            player.inv["steroids"] = number
                        elif x == "p":
                            misc.distance = number
                        elif x == "q":
                            misc.difficulty = number
                        elif x == "r":
                            if "bullets" not in words:
                                words.append("bullets")
                            player.inv["bullets"] = number
                        elif x == "s":
                            print("Gun has been added")
                            player.gun = True







        else:
            #Event start
            print("\n\n\n\n\nYou venture forth into the murky alleyways")
            last = encounterpick(last)
            misc.distance += 1
            if misc.distance > misc.difficulty:
                misc.difficulty = misc.distance
            player.hunger -= 10
            if player.inv["charm"] > precount:
                player.luck += 1
            if player.inv["charm"] < precount:
                player.luck -= 1

            if stalking.switch == True:
                time.sleep(para.Mwait)
                stalking.text[stalking.counter]()
                stalking.counter += 1


def gamend():
    if misc.distance >= 50:
        ZathKopchyla()

    elif player.hunger <= 0:
        print("Your hunger has grown too great and cannot be ignored any longer")
        time.sleep(1)
        print("Collapsing onto the ground, the world grows distant as you starve to death")
        time.sleep(1)
        print("GAME OVER")

    elif player.sanity <= 0:
        print("You have completely gone insane")
        time.sleep(1)
        print("Shadows and hallucinations dance in front of you as reality crumbles")
        time.sleep(1)
        print("A giant hand slowly extends towards you, but you find yourself in no position to stop it")
        time.sleep(1)
        print("From this day on, your body no longer belongs to you.")
        time.sleep(1)
        print("GAME OVER")
#

    print("Final score:", misc.distance)
    time.sleep(3)
    print("Application will close in 5 seconds")
    time.sleep(5)