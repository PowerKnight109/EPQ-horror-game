import time
from parameters import para, misc
def intro():
    print("ETERNAL HUNGER")
    time.sleep(para.Mwait)
    print("You wake up")
    time.sleep(para.Mwait)
    print("You sit in a dingy, rot-infested room")
    time.sleep(para.Mwait)
    print("Corpses and strange runes are strewn about")
    time.sleep(para.Mwait)
    print("You pick up a dagger from one of the corpses and step outside")
    time.sleep(para.Mwait)
    input("Press enter to take a step forward\n")

    #Loop ends when the player reaches 50m, or when health, hunger or stamina reach 0.
     #Will have loop end at max doom later


from character_sheets import player


def gameloop():
    import time
    import random
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
        print("\n\n\n\n\nYou have traveled", misc.distance, "meters")
        print("Health:", str(player.health) + "/" + str(player.maxhealth))
        print("Hunger:", player.hunger)
        print("Sanity:", player.sanity)
        #print("press enter to step forward")
        print("enter 'I' to access inventory")
        proceed = input().lower()

        if proceed == "i":
            from invmenu import inventory
            inventory()

        else:
            #Event start
            print("\n\n\n\n\nYou venture forth into the murky alleyways")
            from encounters import encounterpick
            last = encounterpick(last)
            misc.distance += 1
            if misc.distance > misc.difficulty:
                misc.difficulty = misc.distance
            player.hunger -= 5
            if player.inv["charm"] > precount:
                player.luck += 1
            if player.inv["charm"] < precount:
                player.luck -= 1

            time.sleep(para.Mwait)
            from parameters import stalking
            if stalking.switch == True:
                stalking.text[stalking.counter]()
                stalking.counter += 1


def ending():
    if misc.distance >= 50:
        print("You made it!")

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