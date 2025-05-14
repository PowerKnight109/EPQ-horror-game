import time
from parameters import para, misc
def intro():
    import time
    from parameters import para
    print("ETERNAL HUNGER")
    # print("You wake up")
    # time.sleep(para.Lwait)
    # print("You sit in a dingy, rot-infested room")
    # time.sleep(para.Lwait)
    # print("Corpses and strange runes are strewn about")
    # time.sleep(para.Lwait)
    # print("You pick up a dagger from one of the corpses and step outside")
    # time.sleep(para.Lwait)
    # input("Press enter to take a step forward\n")
    # Loop ends when the player reaches 50m, or when health, hunger or stamina reach 0.
    # Will have loop end at max doom later


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

    while misc.distance < 50 and player.health > 0 and player.hunger > 0 and player.sanity > 0:
        time.sleep(para.Swait)

        print("")
        print("")
        print("")
        print("")
        print("")
        print("You have traveled", misc.distance, "meters")
        print("Health:", str(player.health) + "/" + str(player.maxhealth))
        print("Hunger:", player.hunger)
        print("Sanity:", player.sanity)
        print("press enter to step forward")
        print("enter 'I' to access inventory")
        proceed = input().lower()

        if proceed == "i":
            from invmenu import inventory
            inventory()

        else:
            #Event start
            print("")
            print("")
            print("")
            print("")
            print("")
            print("You venture forth into the murky alleyways")
            from encounters import encounterpick
            encounterpick()

            misc.distance += 1
            if misc.distance > misc.difficulty:
                misc.difficulty = misc.distance
            player.hunger -= para.smallchange


def ending():
    if misc.distance >= 50:
        print("You made it!")

    elif player.hunger <= 0:
        print("Your hunger has grown too great and cannot be ignored any longer")
        time.sleep(1)
        print("Collapsing onto the ground, the world grows distant as you starve to death")
        time.sleep(1)
        print("GAME OVER")

    elif player.hunger <= 0:
        print("You have completely gone insane")
        time.sleep(1)
        print("Shadows and hallucinations dance in front of you as reality crumbles")
        time.sleep(1)
        print("A giant hand slowly extends towards you, but you find yourself in no position to stop it")
        time.sleep(1)
        print("From this day on, your body no longer belongs to you.")
        time.sleep(1)
        print("GAME OVER")
