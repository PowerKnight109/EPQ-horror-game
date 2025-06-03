from character_sheets import player
from parameters import para, misc
import time
import random
from combat import fight

# def restore(statname, stat, value, max):
#     x = stat
#     stat += value
#     if stat > max:
#         stat = max
#     print("["+statname,"+"+str(stat-x)+"]")

class encounters:
    def __init__(self, diff, san, name):
        self.diff = diff
        self.san = san
        self.name = name
        # diff = difficulty (number of steps until event can be included)
        # san = sanity (Maximum sanity value event can occur at)
        # fight = Whether event is a combat encounter or not (will be used when an event outcome leads to random fight)
        # name = name of encounter


class flavourc(encounters):
    def __init__(self):
        super().__init__(1, 101, "flavour")
    def text(self):
        print("gloom and paranoia fill the air")



class Nsaneflavourc(encounters):
    def __init__(self):
        super().__init__(1, 50, "Nsaneflavour")
    def text(self):
        print("The walls of the alley seem to move within themselves, twisting and turning before your eyes")
        time.sleep(para.Mwait)
        print("You hear strange whispers calling out to you, but they disappear whenever you try to focus on them")
        time.sleep(para.Mwait)
        print("Are you going insane?")

class eldritchvisionsc(encounters):
    def __init__(self):
        super().__init__(1, 50, "Nsaneflavour")
    def text(self):
        print("Strange images flash into your head")
        time.sleep(para.Mwait)
        print("Masses of tentacles, cities from worlds far beyond your own, and languages written by civilisations long past")
        time.sleep(para.Mwait)
        print("Your mind screams as you drop to the floor")
        print("Such knowledge was never meant to be peered with mortal eyes")
        time.sleep(para.Swait)
        print("[Sanity -"+str(para.smallchange)+"]")
        player.sanity -= para.smallchange


class foodfindc(encounters):
    def __init__(self):
        super().__init__(1, 101, "meat")
    def text(self):
        print("You found some meat!")
        player.inv["meat"] += (1+player.luck)

class pillfindc(encounters):
    def __init__(self):
        super().__init__(99, 101, "Nsaneflavour")
    def text(self):
        print("You found some pills!")
        player.inv["pills"] += (1+player.luck)

class bandagefindc(encounters):
    def __init__(self):
        super().__init__(99, 101, "bandages")
    def text(self):
        print("You found some bandages!")
        player.inv["bandages"] += (1+player.luck)

class goldfindc(encounters):
    def __init__(self):
        super().__init__(1, 101, "goldfind")
    def text(self):
        print("You found some gold!")
        player.gold += (1+player.luck)

class itemfindc(encounters):
    def __init__(self):
        super().__init__(1, 101, "itemfind")
    def text(self):
        from invmenu import words
        new = random.randint(0, len(words) - 5)
        print("You found some", words[new])
        player.inv[words[new]] += 1
        time.sleep(para.Mwait)

class stargazec(encounters):
    def __init__(self):
        super().__init__(1, 101, "stargaze")
    def text(self):
        print("You look up at the night sky, illuminated by the glow of the starlight")
        time.sleep(para.Mwait)
        print("Wait, those aren't stars...")
        time.sleep(para.Mwait)
        print("Upon closer inspection, you find the night sky dotted with thousands of glowing eyes, their gaze fixed upon you")
        time.sleep(para.Mwait)
        print("[Sanity -"+str(para.smallchange)+"]")
        player.sanity -= para.smallchange

class slimec(encounters):
    def __init__(self):
        super().__init__(2, 101, "slime")
    def text(self):
        print("A black slime drips down")
        from character_sheets import slime
        time.sleep(para.Mwait)
        #print(".................................................................\n...........................::::--:::.............................\n.........................::*#%%%##%#=::..........................\n................:::...::=#%%%%%%%%%%%%@%=:::.....................\n.............::::+#*-=*#%%#%%#%%%%%%%%%%%%*:.::::::..............\n..........:-*####%%%%%%##%%%%%%%%%%%%%%%%%%%%#%%##%*:............\n.........:+%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#:...........\n.........:*%%%%%%%%%#%%%%%%%%%%%####%%%@@@%%%%%%%%%%%=:..........\n.........:#%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*#%%%%%%%%%%#%#-:........\n.......::*%%%%%%%%%%%%%%%%%%%%%%%%%%+-::::::-#%@%%%%%%%#-........\n......:=#%%%%%%%%%###%%%%%%%%%%%%%%-::::+##*::+%@%%%%%%%%:.......\n......-#%%##%%%%%%%%%%%%%%%%%%%%%%*::::-@@@@@::%%%%%@%%%%:.......\n.....:%%%%%%%%%%#%%%%%%%%%%%%%%%%%@:::::::+-:::*@%%#%%%%%-.......\n....:*%%%%%%%%%%%@%%%@@%##%%%%%##%@%=::::::::::%@%%%#%%%%*::::...\n....-#%%%%%##%%#-::::-==#%%%%%%%%%%%%+=::::::-#@%%%%%@%%%%*......\n...:+%%%%@%%%%-+%#=:::=#@%%%%%%%%%%%%%##****%@@#%%#%%%%%%%%-.....\n...:*%%#%%%%#--@@@+-+@@%@%%%%%%%%%%%%%%%%%%%%%%#%%%%%#%%%%%+::::.\n...:#%#%%%#%#+=+*#%%@%%%%%%%%%%%%%%%%%%%%%%%%%%%#%%%%#%%%%%-::::.\n...:*%%%%%%%%@@@%%%%@%%%%%%%%%%%%%%#%%%%%%%%%%%%##%%##%%%%%:.....\n...:*%%%%%%#%%%%%%%%%%%%%%%##%%%%%=-#%#=*%%%%%%%%%%%%%%%%%*:::...\n...:*%%%%%%%%%%%%%%%%%%%%%--+%=#%*--+*--=%+#%%%%%%%%%%%%%%=......\n...:=%%%%%%%%%%%%%%%#+%+*+---*-=%+--+%=-*%-+%*%%%%%%%@%%%#-......\n....:%%%%%%%%%%%%%%%--=------*%%%%%%%%%%%%%%%%%%%%%%%%%%%*:......\n....:#%%%%%@%%%%%%=%**#%%%%%%#--%#%%%%--*@#%%%%%%%%%%%%%%*:......\n....:*%%%%%+%%%%%%%%-%+-#+#%%=----#@*%=*%%%%%%###%%%%%%%%*:......\n....:-@%%%+:-#%%%%%%%%+-=+*%%%#%%#%%%%%%%%%%%%%%%%%*+%%%%*:......\n.....:#%%#:..:*%%%%%%%%+%%%%%%%%%%%%%%%%%%%%%%%%%%=::#%%%+:......\n.....:=%%*::..::+%%%%%#%%%%%%%%%#%%%%%#%%%%%%%%%#-::::%%%=.......\n......-%%+:......:+%%%%%%%%%%%%%%@%%%%%%%%%%%*%%::...:+%%=.......\n.....::#%+:.......::+%%%%%%%%=%%%@%%%%%%%%#+*%%=::...:=%%-.......\n......:+%*:.........:+#-:*%%%-%%%*+%+::#*:..:#%:.....:=%%=:......")
        if fight(slime) == True:
            slime.health = slime.maxhealth
            eat = input("The remains of the slime lie in a puddle before you\nA: consume\nB: leave\n").lower()
            if eat == "a":
                print("You scoop up the goopy remains of the slime and gulp it down")
                time.sleep(para.Mwait)
                print("The acidic body of the slime burns you from the inside out as it slides into your stomach")
                time.sleep(para.Swait)
                print("[Hunger +5]")
                player.hunger += 5
                print("[Health -3]")
                player.health -= 3
                time.sleep(para.Mwait)
                print("Why did you think that would be a good idea?")
                time.sleep(para.Swait)
                print("[Sanity -"+str(para.largechange)+"]")
                player.sanity -= para.largechange
            else:
                print("You're done here")

class zombiec(encounters):
    def __init__(self):
        super().__init__(2, 101, "zombie")
    def text(self):
        print("You see a figure up ahead")
        time.sleep(para.Mwait)
        print("It mindlessly shuffles towards you, with every step it takes looking like it requires a colossal amount of effort")
        time.sleep(para.Mwait)
        print("There is no humanity left in it's eyes, only hunger.")
        time.sleep(para.Swait)
        x = input("A: Attack\nB: Decieve\nC: Run\n").lower()
        battle = False
        if x == "a":
            print("You attack the zombie!")
            battle = True
        elif x == "b":
            print("You outstretch your arms and slowly walk forwards, doing your best impression of a walking corpse")
            time.sleep(para.Mwait)
            print("...")
            time.sleep(para.Mwait)
            print("Your skills aren't going to be getting you any Oscars anytime soon")
            time.sleep(para.Mwait)
            print("The creature attacks!")
            time.sleep(para.Swait)
            print("[Health -"+str(para.smallschange)+"]")
            player.health -= para.smallschange
            time.sleep(para.Swait)
            battle = True
        elif x == "c":
            print("You easily get away from the creature")
            time.sleep(para.Mwait)
            print("However, all of that running has used up more of your energy")
            time.sleep(para.Swait)
            print("[Hunger -"+str(para.smallchange)+"]")
            player.hunger -= para.smallchange

        if battle == True:
            from character_sheets import zombie
            #print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@........@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@............@@.....@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@................@@.......@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@............@@@@.............@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@....@....@@@@@@@@@@....@@.........@@@@@@@@@@...@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@.......@@@@@@@@@@@@@@@@@...@@......@@@@@@@@@@@@@@@..@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@......@@@@@@@@@@@@@@@@@@@............@@@@@@@@@@@@@@@@@@..@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@.....@@@@@@@@@@@@@.....@@@............@@@@@@@@@@@@@@@@@@@@...@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@....@@@@@@@@@@@@@...@@..@@.........@@@@@@@@@@@@.....@@@@@@@@....@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@...@@@@@@@@@@@@@@......@@.............@@@..@@@@..@@..@@@@@@@@.....@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@..@@@@@@@@@@@@@@@@@@@@@..................@@@.@@@....@@@@@@@@@@@......@@@@@@@@@@@@@@@@@\n@@@@@@@@@...@@@@@@@@@@@@@@@..........................@@@..@@@@@@@@@@@@@@@.......@@@@@@@@@@@@@@@@\n@@@@@@@@.@@@@@........@@@..............................@@@@.....@@@@@@@@@@@......@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@.......@@@@.....@@@@.......................@@...............@@@......@@@@@@@@@@@@@@\n@@@@@@@@...........@@...@@@@@..........................@@..................@@@....@@@@@@@@@@@@@@\n@@@@@@@................@@@............................@.....................@@@....@@@@@@@@@@@@@\n@@@@@@...............@@@..........................@@@@....................@@@@.....@@@@@@@@@@@@@\n@@@@@@..............@@...........................@@@@@@...............@@@@@@@@.....@@@@@@@@@@@@@\n@@@@..............@@@@......@@..................@@@@@@@@@@...........@@@@@@@@@.....@@@@@@@@@@@@@\n@@@................@@@@....@@@@@@@@............@@@@@@@@@@@@..........@@@@@@@@@.........@@@@@@@@@\n@@@@@@..............@@...@@@@@@@@@@@@@@@@@..@@@@@@@@@@@@@@@@@.......@@@@@@@@@@........@@@@@@@@@@\n@@....@.............@@..@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@....@@@..@@@@@@@@\n@@....@............@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..@@.....@@@@@@@\n@@....@...........@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.@......@@@@@@@\n@@@...@@.........@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.....@@@@@@@@\n@@@.....@@@.....@@@@@...@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@......@@@@@@@@\n@@@@.......@@@@@@@@@.......@@@@@@@@@@@@@@@@@@@@@@@@@@@@@......@@@@@@@@@@@@@@@@@@@@.....@@@@@@@@@\n@@@@@......@@@@@@@@...........@@@@@@@@@@@@@@@@@@@@@@@@............@@@@@@@@@@@@@@@@....@@@@@@@@@@\n@@@@@@....@@@....................@@@@@@@@@@@@@@@@@@..................@@@@@@@@@@@@.....@@@@@@@@@@\n@@@@@@@@@.@@@......................@@@@@@@@@@@@@......................@@@@@@@@@@@....@@@@@@@@@@@\n@@@@@@@@@@@@..........................@@@@@@@@........................@@...@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@.............................@@@@........................@@@.....@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@............................@@@.........................@@@........@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@...........................@@@@@....................@@@@@@.......@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@............................@@@@@@.................@@@@@.....@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@...........................@@@@@...............@@@@@@.@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@.......................@@@@@................@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@.................@@@@@@.................@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@............@@@@@@@................@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@...........@@@@@@@@...........@@.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@...@@@......@@@@@@@@......@@........@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@........@@....@@@@@@@@.@@............@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@..............@@@@@@@@@@...............@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@........................................@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@..........................................@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            if fight(zombie) == True:
                zombie.health = zombie.maxhealth
                x = input("The unmoving body of the zombie lies before you\nA: Consume\nB: Loot\nC: Leave\n").lower()
                if x == "c":
                    print("You move on")
                else:
                    if random.randint(1,100)+player.luck > 10:
                        if x == "b":
                            print("You loot the body for supplies")
                            from invmenu import words
                            time.sleep(para.Mwait)
                            new = random.randint(0, len(words) - 5)
                            print("You found some", words[new])
                            player.inv[words[new]] += 1

                        elif x == "a":
                            print("Can you really bring yourself to eat something which was once human?")
                            time.sleep(para.Mwait)
                            print("The pain in your stomach answers your question as you begin to rip the body apart for meat")
                            time.sleep(para.Mwait)
                            print("Your stomach is satisfied, but your conscience isn't")
                            time.sleep(para.Mwait)
                            #restore("Hunger", player.hunger,  para.largerestore, 100)
                            a = player.hunger
                            player.hunger += para.largerestore
                            if player.hunger > 100:
                                player.hunger = 100
                            print("[Hunger restored by", str(player.hunger - a) + "]\n")
                            print("[Sanity -"+str(para.largechange)+"]")
                            player.sanity -= para.largechange

                    else:
                        print("The zombie starts to move again!")
                        fight(zombie)

class shadowc(encounters):
    def __init__(self):
        super().__init__(2, 50, "shadow")
    def text(self):
        print("The shadows begin to move towards you")
        time.sleep(para.Mwait)
        #print("....................................................................................................\n....................................................................................................\n....................................................................................................\n....................................................................................................\n....................................................................................................\n....................................................................................................\n....................................................................................................\n.............................................@@@@@@@@@@.............................................\n.......................................@@@@@@@@......@@@@@@@@.......................................\n.....................................@@@....................@@@.....................................\n....................................@..........................@....................................\n...................................@.........@@......@@@........@...................................\n..................................@.......@@@@@.......@@@@.......@..................................\n..................................@.......@@............@@.......@..................................\n..................................@..............................@..................................\n..................................@..............................@..................................\n..................................@..............................@..................................\n..................................@..............................@..................................\n..................................@..@@....................@@....@..................................\n..................................@...@@@@@@@@@@@@@@@@@@@@@@.....@..................................\n..................................@.......@@@@@@@@@@@@@@@........@..................................\n...................................@........@@@@@@@@@@@@........@...................................\n....................................@@@......................@@@....................................\n........................................@@@@.............@@@@.......................................\n.............................................@@@@@@@@@@@@...........................................\n............................................@...........@...........................................\n............................................@...........@...........................................\n..........................................@@............@@..........................................\n......................................@@@@................@@@@......................................\n...............................@@@@@@@@......................@@@@@@@@...............................\n..........................@@@@@@....................................@@@@@@..........................\n.......................@@@@..............................................@@@@.......................\n.....................@@@....................................................@@@.....................\n....................@@@......................................................@@@....................\n...................@@@........................................................@@@...................")

        from character_sheets import shadow
        fight(shadow)

class lootcorpsec(encounters):
    def __init__(self):
        super().__init__(2, 101, "lootcorpse")
    def text(self):
        print("You find a corpse lying on the ground.")
        time.sleep(para.Mwait)
        print("It may have valuable items for your survival.")
        time.sleep(para.Swait)
        print("A: loot the corpse\nB: consume the corpse\nC: leave")
        choice = input().lower()
        if choice == "c":
            print("You aren't going to risk it")
        else:
            if random.randint(1, 100) + player.luck > 25 - (misc.difficulty / 10):
                if choice == "a":
                    print("You loot the corpse for items")
                    time.sleep(para.Mwait)
                    from invmenu import words
                    new = random.randint(0, len(words)-5)
                    print("You found some", words[new])
                    player.inv[words[new]] +=1
                    time.sleep(para.Mwait)
                    print("You can't get the image of their lifeless face out of your head")
                    time.sleep(para.Mwait)
                    print("[Sanity -"+str(para.smallchange)+"]")
                    player.sanity -= para.smallchange

                elif choice == "b":
                    print("Are you really going to resort to cannibalism?")
                    time.sleep(para.Mwait)
                    print("Well, you can't be picky in this world")
                    time.sleep(para.Mwait)
                    print("You close you eyes and sink your teeth in, forcing each bite down your throat")
                    time.sleep(para.Mwait)
                    x = player.hunger
                    player.hunger += para.largerestore
                    if player.hunger > 100:
                        player.hunger = 100
                    print("[Hunger +"+str(player.hunger - x)+"]")
                    print("[Sanity -"+str(para.largechange)+"]")
                    player.sanity -= para.largechange
            else:
                print("The corpse got up and attacked!")
                time.sleep(para.Mwait)
                if misc.difficulty < 35:
                    #print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@........@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@............@@.....@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@................@@.......@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@............@@@@.............@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@....@....@@@@@@@@@@....@@.........@@@@@@@@@@...@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@.......@@@@@@@@@@@@@@@@@...@@......@@@@@@@@@@@@@@@..@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@......@@@@@@@@@@@@@@@@@@@............@@@@@@@@@@@@@@@@@@..@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@.....@@@@@@@@@@@@@.....@@@............@@@@@@@@@@@@@@@@@@@@...@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@....@@@@@@@@@@@@@...@@..@@.........@@@@@@@@@@@@.....@@@@@@@@....@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@...@@@@@@@@@@@@@@......@@.............@@@..@@@@..@@..@@@@@@@@.....@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@..@@@@@@@@@@@@@@@@@@@@@..................@@@.@@@....@@@@@@@@@@@......@@@@@@@@@@@@@@@@@\n@@@@@@@@@...@@@@@@@@@@@@@@@..........................@@@..@@@@@@@@@@@@@@@.......@@@@@@@@@@@@@@@@\n@@@@@@@@.@@@@@........@@@..............................@@@@.....@@@@@@@@@@@......@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@.......@@@@.....@@@@.......................@@...............@@@......@@@@@@@@@@@@@@\n@@@@@@@@...........@@...@@@@@..........................@@..................@@@....@@@@@@@@@@@@@@\n@@@@@@@................@@@............................@.....................@@@....@@@@@@@@@@@@@\n@@@@@@...............@@@..........................@@@@....................@@@@.....@@@@@@@@@@@@@\n@@@@@@..............@@...........................@@@@@@...............@@@@@@@@.....@@@@@@@@@@@@@\n@@@@..............@@@@......@@..................@@@@@@@@@@...........@@@@@@@@@.....@@@@@@@@@@@@@\n@@@................@@@@....@@@@@@@@............@@@@@@@@@@@@..........@@@@@@@@@.........@@@@@@@@@\n@@@@@@..............@@...@@@@@@@@@@@@@@@@@..@@@@@@@@@@@@@@@@@.......@@@@@@@@@@........@@@@@@@@@@\n@@....@.............@@..@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@....@@@..@@@@@@@@\n@@....@............@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..@@.....@@@@@@@\n@@....@...........@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.@......@@@@@@@\n@@@...@@.........@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.....@@@@@@@@\n@@@.....@@@.....@@@@@...@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@......@@@@@@@@\n@@@@.......@@@@@@@@@.......@@@@@@@@@@@@@@@@@@@@@@@@@@@@@......@@@@@@@@@@@@@@@@@@@@.....@@@@@@@@@\n@@@@@......@@@@@@@@...........@@@@@@@@@@@@@@@@@@@@@@@@............@@@@@@@@@@@@@@@@....@@@@@@@@@@\n@@@@@@....@@@....................@@@@@@@@@@@@@@@@@@..................@@@@@@@@@@@@.....@@@@@@@@@@\n@@@@@@@@@.@@@......................@@@@@@@@@@@@@......................@@@@@@@@@@@....@@@@@@@@@@@\n@@@@@@@@@@@@..........................@@@@@@@@........................@@...@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@.............................@@@@........................@@@.....@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@............................@@@.........................@@@........@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@...........................@@@@@....................@@@@@@.......@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@............................@@@@@@.................@@@@@.....@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@...........................@@@@@...............@@@@@@.@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@.......................@@@@@................@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@.................@@@@@@.................@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@............@@@@@@@................@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@...........@@@@@@@@...........@@.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@...@@@......@@@@@@@@......@@........@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@........@@....@@@@@@@@.@@............@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@..............@@@@@@@@@@...............@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@........................................@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@..........................................@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                    from character_sheets import zombie
                    fight(zombie)
                    zombie.health = zombie.maxhealth
                else:
                    from character_sheets import skinwalker
                    fight(skinwalker)

class lore1c(encounters):
    def __init__(self):
        super().__init__(3, 101, "lore1")
    def text(self):
        #print("lore1: paper about energy in sea")
        print("You find an old newspaper on the ground")
        time.sleep(para.Mwait)
        read = input("Read it?\nA: Yes\nB: No\n").lower()
        if read == "a":
            print('                          "POWER CRISIS SAVED!"')
            time.sleep(para.Mwait)
            print("'For all to long now, Arkham City has been plagued by a looming issue hanging over all our heads'")
            time.sleep(para.Mwait)
            print(
                "'One that, in spite of our best scientist's work, has continued to evade us, as we draw ever closer to certain doom.'")
            time.sleep(para.Mwait)
            print(
                "'I am of course talking about the Great Energy Crisis, and our city's struggle to find new energy sources to sustain itself, while our remaining stores rapidly wither away.'")
            time.sleep(para.Mwait)
            print(
                "'While we were thought to run out in 50 years, worry not! Vexon Industries, a superpower in the oil drilling industry claims that it has uncovered a new, renewable source of energy which can last us for generations!'")
            time.sleep(para.Mwait)
            print(
                "'This new type of energy, which they have dubbed 'zathene energy' was discovered in one of their plants off the east coast, and is reportedly 'fully renewable', producing 'trillions of gigajoules of energy per second'")
            time.sleep(para.Mwait)
            print("'At last, the people of Arkham can sleep soundly at night, knowing that their future is safe.'")
        else:
            print("There's no time")

class shrinec(encounters):
    def __init__(self):
        super().__init__(3, 101, "shrine")
    def text(self):
        print("You find a shrine to a local diety")
        time.sleep(para.Mwait)
        print("A: Offer some money")
        print("B: Offer some food")
        print("C: Loot the shrine")
        print("D: move on")
        shrine = input().lower()
        if shrine == "a":
            print("You have", player.gold, "gold")
            print("how much money will you offer?")
            print("(Type 0 to go back)")
            a = int(input())
            if a <= 0:
                print("You change your mind")
            elif a > player.gold:
                print("You don't have enough money!")
            else:
                player.gold -= a
                player.luck += a
                print("You offer", a, "gold to the shrine")
                time.sleep(para.Mwait)
                print("You feel blessed")
                time.sleep(para.Swait)
                print("[Luck +" + str(a) + "]")
        elif shrine == "b":
            if player.inv.food > 0:
                print("How much food will you offer?\n(type 0 to go back)")
                a = int(input())
                if a > player.inv["meat"]:
                    print("You don't have enough food!")
                elif a <= 0:
                    print("You change your mind")
                else:
                    player.inv["meat"] -= a
                    player.luck += a
                    print("You offer some food to the shrine")
                    time.sleep(para.Mwait)
                    print("You feel blessed")
                    time.sleep(para.Swait)
                    print("[Luck +" + str(a) + "]")
        elif shrine == "c":
            print("Nobody's gonna care if you take a few things right?")
            time.sleep(para.Swait)
            print("Besides, you need these supplies more than some nonexistant gods")
            time.sleep(para.Mwait)
            print("[Gold +" + str(para.smallschange) + "]")
            player.gold += para.smallschange
            time.sleep(para.Swait)
            print("As you leave, you are suddenly assaulted by a wave of regret")
            time.sleep(para.Mwait)
            print("You feel damned")
            time.sleep(para.Swait)
            print("[Luck -" + str(para.smallschange) + "]")
            player.luck -= para.smallschange

class konamic(encounters):
    def __init__(self):
        super().__init__(3, 101, "c-ritual")
    def text(self):
        print("You see some writing etched onto a wall")
        time.sleep(para.Mwait)
        print('It reads "^^vv<><>BA"')
        code = ["^", "^", "v", "v", "<", ">", "<", ">"]
        fail = False
        codewords = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth"]
        time.sleep(para.Mwait)
        print("These seem to be the moves to an ancient counteritual to stop the apocalypse")
        time.sleep(para.Mwait)
        print("Perform the ritual?")
        time.sleep(para.Swait)
        print("A: Yes")
        print("B: No")
        x = input().lower()
        if x == "a":
            for i in range(25):
                print("\n")
            for i in range(8):
                dance = input("Please enter the " + codewords[i] + " move of the ritual\n").lower()

                if dance == code[i]:
                    continue
                else:
                    fail = True
                    break
            if fail == False:
                print("Is that all?")
                time.sleep(para.Swait)
                print("A: Yes")
                dance = input("B: No\n").lower()
                if dance == "b":
                    print("What about now?")
                    time.sleep(para.Swait)
                    print("A: Yes")
                    dance = input("B: No\n").lower()
                    if dance == "a":
                        print("You completed the ritual")
                        time.sleep(para.Swait)
                        # print("D00M -" + str(para.smallschange) + "]")
                        # Doom -= para.v.smallchange
                        print("[Luck +"+str(para.smallschange)+"]")
                        player.luck += para.smallschange

                    else:
                        fail = True
                else:
                    fail = True

            if fail == True:
                print("You failed the ritual")
                time.sleep(para.Swait)
                # print("D00M +" + str(para.smallschange) + "]")
                # Doom += para.smallchange
                print("[Luck -" + str(para.smallschange) + "]")
                player.luck -= para.smallschange


        else:
            print("You aren't going to make a fool of yourself trying to do some ridiculous dance")
            time.sleep(para.Swait)
            print("Besides, it probably wouldn't have worked anyway")

class drinkc(encounters):
    def __init__(self):
        super().__init__(3, 101, "drink")
    def text(self):
        print("You have been walking for a long time, and you find yourself in dire need of water")
        time.sleep(para.Mwait)
        print("Ahead of you, you spot an old faucet connected to a wall.")
        time.sleep(para.Mwait)
        print("Drink from the faucet?")
        time.sleep(para.Swait)
        print("A: Yes")
        print("B: No")
        x = input().lower()
        if x == "a":
            print("You turn the faucet")
            time.sleep(para.Lwait)
            if random.randint(0, 100) + player.luck > 25:
                print("Cool, refreshing water flows down the tap, revitalising your body and mind")
                time.sleep(para.Mwait)
                print("[Sanity +" + str(para.smallchange) + "]")
                player.sanity += para.smallchange
                if player.sanity > 100:
                    player.sanity = 100
            else:
                print("The faucet turns on, but it doesn't produce water")
                time.sleep(para.Mwait)
                print("Instead, blood flows down, coating your hands and feet")
                time.sleep(para.Mwait)
                print("[Sanity -" + str(para.smallchange) + "]")
                player.sanity -= para.smallchange
        else:
            print("You decide to ignore it, the water isn't safe.")
            time.sleep(para.Mwait)
            print("But your thirst has become dire, and you find yourself growing weaker because of it")
            time.sleep(para.Mwait)
            print("[Health -" + str(para.smallschange) + "]")
            player.health -= para.smallschange

class deersacc(encounters):
    def __init__(self):
        super().__init__(4, 101, "deersac")
    def text(self):
        print("You see a young fawn strapped to an altar")
        time.sleep(para.Mwait)
        print("Was there some sort of sacrifice here?")
        time.sleep(para.Mwait)
        x = input("A: Complete the sacrifice\nB: Consume\nC: Free the deer\n").lower()
        if x == "a":
            print("You raise your dagger and plunge it into the deer's heart")
            time.sleep(para.Mwait)
            print("The fawn's blood flows freely down the altar")
            print("The gods are pleased with you, but at what cost")
            time.sleep(para.Mwait)
            print("[Luck +"+str(para.largeschange)+"]")
            print("[Sanity -" + str(para.smallchange) + "]")
            player.luck += para.largeschange
            player.sanity -= para.smallchange

        elif x == "b":
            print("You raise your dagger and plunge it into the fawn's heart")
            time.sleep(para.Mwait)
            print("But before the deer's blood can flow down the altar, you snatch it up and greedily dig in")
            time.sleep(para.Mwait)
            print("It had been too long since you had last eaten a normal animal, you had nearly forgotten the taste")
            time.sleep(para.Swait)
            a = player.hunger
            player.hunger += para.smallrestore
            if player.hunger > 100:
                player.hunger = 100
            print("[Hunger restored by", str(player.hunger - a) + "]")
            print("[Sanity -"+str(para.smallchange)+"]")
            player.sanity -= para.smallchange

        elif x == "c":
            print("You undo the baby deer's bindings and let it walk free")
            time.sleep(para.Mwait)
            print("It soothes your heart that something so innocent could exist in a world so cruel")
            time.sleep(para.Swait)
            print("[Sanity +"+str(para.smallrestore)+"]")
            player.sanity += para.smallchange

class batterc(encounters):
    def __init__(self):
        super().__init__(5, 101, "batter")
    def text(self):
        print("A man calls out to you")
        time.sleep(para.Mwait)
        print("His face is covered by a mask bearing a wide toothy grin, and in his hands he clutches a bloodied baseball bat.")
        time.sleep(para.Mwait)
        print("It's clear to you that this man may not have the most savoury intentions.")
        time.sleep(para.Swait)
        x = input("Do you:\nA: Attack\nB: Hide\nC: Run\n").lower()
        combat = False
        if x == "a":
            print("You attack the masked man")
            combat = True
        elif x == "b":
            print("You run into a nearby building to hide")
            time.sleep(para.Mwait)
            print("Finding yourself in a public bathroom, you run into the furthest cubicle and shut the door")
            time.sleep(para.Mwait)
            print("Soon, you hear footsteps approaching")
            time.sleep(para.Mwait)
            for i in range(6):
                if i == 6:
                    print("It's your door")
                    time.sleep(para.Mwait)
                    print("You find yourself staring directly at the lifeless mask of your assailant")
                    time.sleep(para.Swait)
                    print("[Sanity -"+str(para.smallchange)+"]")
                    player.sanity -= para.smallchange
                    combat = True
                else:
                    door = random.randint(0, 6-i)
                    if door == 0:
                        print("The footsteps fade away")
                        break
                    else:
                        print("'BAM!'")
                        time.sleep(para.Swait)
                        print("You hear the door to one of the bathroom stalls get slammed open")
                        time.sleep(para.Lwait)

        elif x == "c":
            print("You run as fast as you can in the opposite direction, and the masked man gives chase")
            time.sleep(para.Mwait)
            print("He seems to enjoy toying with you, slowing down until he's nearly out of sight before speeding up again")
            time.sleep(para.Mwait)
            print("Suddenly, you hear a loud snapping sound behind you, alongside the crunching of bones")
            time.sleep(para.Mwait)
            print("The alleyway you just ran through had been blocked off by a vertical row of teeth")
            time.sleep(para.Mwait)
            print("All that remained of your pursuer was a single arm, poking out from a gap in the teeth.")
            time.sleep(para.Mwait)
            print("[Hunger -"+str(para.smallchange)+"]")
            print("[Sanity -"+str(para.smallchange)+"]")
            player.hunger -= para.smallchange
            player.sanity -= para.smallchange
            time.sleep(para.Swait)
            print("Unfortunately, the chase caused you to backtrack through some of the progress you made")
            print("[Distance -3]")
            misc.distance -= 3

        if combat == True:
            #print("..@@@@@@....@.@@@@@@...........@@......................@@@@@....@..@@...........\n.....@@......@@@@@.......................................@@@@@..................\n........@...@@@@@.........................................@@@@@.....@........@@.\n...........@@@@@............................................@@@@@...@....@@.@@..\n..........@@@@@..............................................@@@@@....@@.@@.....\n.........@@@@@.......................................@........@@@@@@@@@@........\n.........@@@@....................................@@@@@.........@@@@@............\n........@@@@.......@@@@@.......................@@@@@@@@.........@@@@@...........\n........@@@.......@@@@@@@......................@@@@@@@@.@........@@@@...........\n.......@@@@.......@@@@@@@@@...................@@@@@@@@@@@.......................\n.......@@@@......@@@@@@@@@@@..................@@@@@@@@@@@.........@.@@@.........\n.......@..........@@@@@@@@@@..................@@@@@@@@@@@.......@.@.............\n.@.@@@@..........@@@@@@@@@@@..................@@@@@@@@@@@.........@..@@.........\n.@@@@..@.........@@@@@@@@@@@@.................@@@@@@@@@@@.........@@@@@........@\n.@@@@.@@@........@@@@@@@@@@@@.................@@@@@@@@@...........@@@@@@.....@@@\n.@@@@.@@@@@.......@@@@@@@@@@@.................@@@@@@@@.@@.........@@@@@@...@@@..\n..@@..@@@@@........@@@@@@@@@@.........@.......@@@@@@@.........@@..@@@@@..@@@....\n.@@@@..@@@@........@..@@@@@@@.....@@@@@@.@@.....@@@@@@.......@...@@@@@@@@@.....@\n.@@@@@.@@@@...........@.@@@......@@@@@@@@@.@................@@@@.@@@@@@@@....@..\n..@@@@.@@@@..@@.................@@@@@@@@@@@@@....@@........@@@@@@@@@@@@.@.......\n.@@@@@.@@@@.@@@@@.......@@@@....@@@@@@@@@@@@....@@@@.........@@@.@@@@@@@@@......\n.@@@@...@@@@.@@@..@......@@@.....@@@@@@@@@@@......@...@@@@...@@..@@@@.@@@@@.....\n.@@@@@.@@@@@.@@....@@.....@........@@@@@@@........@.@@@.....@@@.@@@@..@...@@@@@@\n.@@@@@.@.@@@@@@@...@@@@@............................@.....@@@@@@@@@@..@...@.....\n..@@@@@@.@@@@@@@@......@.@@@@@@.........@@@@@@@@.........@@@@@@@@@@@@@@.@.@.....\n..@@@@.@.@@@@@@@@@@@.........@@.@@@@@@@@@...............@@.@@..@@@@@.....@.@@@..\n..@@@@.@.@@@@@@@@@@@..................@...............@@@...@.@@@@@..........@.@\n.@@@@@@..@@@@@.@@..@@@@.............................@@@@..@..@@@@@.............\n...@@@@@@..@@@@@.@..@@@@@........................@.@@@@...@..@@@@.@.............\n...@.........@@@@.......@@@@.@.......@@@@......@@@@@@.....@.@@@@@.@.............\n....@@.@.......@@@.......@@@@@@@@@@@@@@@@@@@@@@@@@@......@...@@@@...............\n................@@@.@........@@@@@@@@@@@@...@@........@......@@@@...............\n................@@@@.@@.@....................................@@@@...............\n................@@@@@..@.@..........................@@........@@................\n..........@......@@@@@@.@.@..@..........@...@....@@@..........@@................\n.................@@@@@......@@@@@@@@@@@........@@.............@.................\n........@@@@......@.@@@.........@@@.@@@@@@@@....................................\n.....................@@.........................................................\n......................@@........................................................\n.......................@@.......................................................\n................................................................................\n................................................................................")
            from character_sheets import batter
            if fight(batter) == True:
                batter.health = batter.maxhealth
                x = input("The corpse of the masked man lies before you\nA: consume\nB: loot\nC:leave\n").lower()
                if x == "c":
                    print("You proceed forwards")
                else:
                    if random.randint(1, 100) + player.luck > 5:
                        if x == "b":
                            print("You loot the corpse for supplies")
                            from invmenu import words
                            time.sleep(para.Mwait)
                            new = random.randint(0, len(words) - 5)
                            print("You found some", words[new])
                            player.inv[words[new]] += 1

                        elif x == "c":
                            print("What are you thinking? You can't just eat a human!")
                            time.sleep(para.Swait)
                            print("However, after eating nothing but rotten meat for the past few days, your mouth can't help but water at the thought")
                            time.sleep(para.Swait)
                            print("Unable to control your body, you find yourself kneeling besides the corpse")
                            time.sleep(para.Swait)
                            print("No time is wasted cutting out chunks or removing clothes; instead, you immediately sink your teeth in like a wild animal")
                            time.sleep(para.Swait)
                            print("For several minutes you greedily tear into them, until all that remains are bones")
                            time.sleep(para.Swait)
                            print("You are no more man than beast; a slave to your base desires.")
                            time.sleep(para.Lwait)
                            #restore("Hunger", player.hunger, para.largerestore, 100)
                            a = player.hunger
                            player.hunger += para.largerestore
                            if player.hunger > 100:
                                player.hunger = 100
                            print("[Hunger restored by", str(player.hunger - a) + "]")
                            print("[Sanity -40]")
                            player.sanity -= 40

                    else:
                        print("Suddenly, the masked man gets back up!")
                        fight(batter)

class shopc(encounters):
    def __init__(self):
        super().__init__(6, 101, "shop")
    def text(self):
        print("You enter a dingy warehouse.")
        time.sleep(para.Swait)
        print("Chains are strung up all over the walls and ceiling")
        time.sleep(para.Mwait)
        print("In the center of the room, a woman hangs down over a table of items, her limbs bound by several layers of shackles")
        time.sleep(para.Mwait)
        print("Her eyes widen as they fix their gaze on you")
        time.sleep(para.Swait)
        print("PlEaSsSse, FeEl FrEe To BrOwSe My WaReSsS!")
        time.sleep(para.Swait)
        print("A: Shop\nB:Leave\n")
        x = input().lower()
        if x == "a":
            while True:
                print("WhAt WoUlD yOu LiKe To PuRcHaSsSeE?")
                time.sleep(para.Swait)
                print("you have", player.gold, "gold")
                print("- meat(1G)\n- pills(2G)\n- bandages(2G)\n- effigy(0G)\n- charm(3G)\n- steroids(5G)")
                print("type the name of the item you want to purchase")
                browse = input().lower()
                from invmenu import words
                prices = [1, 2, 2, 0, 3, 5]
                if browse in words and prices[words.index(browse)] > player.gold:
                    #print("YoU DoN't HaVe EnOuGhH!")
                    print("ThInK yOu CaN cHeAt MeEe? YoUu lAcK tHe CoInN!!!" )
                elif browse in words:
                    print("You purchased the", browse)
                    print("[Gold -"+str(prices[words.index(browse)])+"]")
                    player.gold -= prices[words.index(browse)]
                    player.inv[browse] += 1
                else:
                    break

        print("CoMe AgAiNn SsOoNn!")

class gnasherc(encounters):
    def __init__(self):
        super().__init__(7, 101, "gnasher")
    def text(self):
        print("You hear a loud crash in front of you")
        time.sleep(para.Mwait)
        print("A humanoid figure steps back, leaving a sizeable dent in the wall it ran into")
        time.sleep(para.Mwait)
        print("The creature's skin is grey and clammy, and its arms have seemingly fused into its body")
        time.sleep(para.Mwait)
        print("The monster is also devoid of facial features, save for a giant mouth taking up its entire face")
        time.sleep(para.Mwait)
        print("The monster begins to prowl, tapping on random objects with its clawed feet and listening out for noise")
        time.sleep(para.Mwait)
        print("Despite standing directly in front of it, the creature doesn't seem to have noticed you yet.")
        time.sleep(para.Mwait)
        x = input("A: Fight\nB: Run\nC: Distraction\nD: Sneak past\n").lower()
        combat = False
        if x == "a":
            print("You run towards the creature")
            combat = True

        elif x == "b":
            print("You decide to run away as fast as you can")
            time.sleep(para.Swait)
            print("Suddenly, you hear a loud screeching noise behind you")
            time.sleep(para.Mwait)
            print("The screeching noise gets louder and louder")
            time.sleep(para.Mwait)
            print("Suddenly, you are hit by the impact of the creature")
            time.sleep(para.Mwait)
            print("Pain surges through your body as you are knocked to the ground from the force of the blow")
            time.sleep(para.Mwait)
            print("[Health -4]")
            player.health -= 4
            combat = True

        elif x == "c":
            while True:
                print("Perhaps if you were to throw something, you could draw the creature's attention away from you")
                time.sleep(para.Swait)
                throw = input("A: Throw gold\nB: Throw item\nC: Throw self\n").lower()
                if throw == "a":
                    if player.gold > 0:
                        print("You throw a piece of gold")
                        time.sleep(para.Mwait)
                        print("The gold makes a loud clanging noise as it hits the floor")
                        time.sleep(para.Mwait)
                        print("The creature suddenly jolts up and charges in the direction of the gold, letting loose an ear-piercing screech")
                        time.sleep(para.Mwait)
                        print("You seize the moment and dash past as fast as you can")
                        time.sleep(para.Swait)
                        print("[Hunger -"+str(para.smallchange)+"]")
                        player.hunger -= para.smallchange
                        print("[Gold -1]")
                        player.gold -= 1
                        break
                    else:
                        print("You don't have enough gold")
                        continue
                elif throw == "b":
                    from invmenu import words
                    while True:
                        hasitems = False
                        for i in range(len(words)):
                            if player.inv[words[i]] > 0:
                                print(words[i] + ":", player.inv[words[i]])
                                hasitems = True

                        if hasitems == True:
                            garbage = input("Type the item you want to throw").lower
                            if garbage in player.inv:
                                print("You throw the", garbage, "at some empty bottles lined up on a nearby window")
                                time.sleep(para.Mwait)
                                print("The bottles fall to the floor with a loud crash, instantly grabbing the monster's attention")
                                time.sleep(para.Mwait)
                                print("With an ear-piercing shriek, the monster charges at the window, crashing through the wall of the house")
                                time.sleep(para.Mwait)
                                print("You make your escape before the dust can settle")
                                time.sleep(para.Swait)
                                print("["+str(garbage), "-1]")
                                player.inv[garbage] -= 1
                                break
                        else:
                            print("You have no items to throw")
                        continue

                else:
                    print("You throw yourself into some nearby boxes, which topple down around you")
                    time.sleep(para.Mwait)
                    print("The creature snaps towards you, and charges at breakneck speed")
                    time.sleep(para.Mwait)
                    print("Before you can pick yourself up, you feel a colossal force ram into you, sending you flying into a wall")
                    time.sleep(para.Swait)
                    print("[Health -4]")
                    player.health -= 4
                    print("You can barely endure the pain in your ribs as you see the monster preparing another charge attack")
                    combat = True

        elif x == "d":
            print("You slowly creep by the creature, being careful as to make as little noise as possible")
            time.sleep(para.Mwait)
            print("You feel the creature's hot breath against your face")
            time.sleep(para.Mwait)
            if random.randint(0, 100) + player.luck > 50:
                print("You manage to carefully sneak ahead, until the creature is out of sight")
                time.sleep(para.Mwait)
                print("You breath a sigh of relief")
            else:
                print("Suddenly, the silence is pierced by a crinkling sound")
                time.sleep(para.Mwait)
                print("You look down, and to your horror you realise your foot has landed on a pile of broken glass")
                time.sleep(para.Mwait)
                print("You look back up and are greeted by the open maw of the creature lunging towards you!")
                time.sleep(para.Mwait)
                print("There's a sickening crunch as its teeth pierce through you, causing a massive surge of pain throughout your body")
                time.sleep(para.Swait)
                print("[Health -4]")
                player.health -= 4
                combat = True


        if combat == True:
            from character_sheets import gnasher
            #print("######%##%%%##%#++.:........:-+*##%######%######%%%%%#%%%#%#\n######%%#%#%##*+-::-----:..:=+++===+*##%%####%%##%%#%%%%%#%%\n###########*=::--:::---:....:-++**++++##%####%%##%#%#%%%%%%%\n##########+::==---.:::----=-:.:=+++*****######%%###%#%%@%#%%\n#######%#+:=+=:...::---======--==+++**####%##%#####%%%##%#%%\n########=+*+--..:=####%@@@@@@%%%#*++###%%%%####%%####%%%%%%#\n#######+***=+==*@#**#*===+%@**#%%@@@@%%%@@@@%#%%%##%%%#%#%%%\n#%####*###***@@@#-:=*-. .-#@+---=+*++@@%%@@@@#%%###%#%%%%%#%\n####%#*%%+#%@@%+*..=*-   .+@+-..:---=*@@@@@@@%########%%%#%#\n######%#%*@@@#-+*:.##=   .=@*-..:-+=-=+%@@@@@@##############\n%%###%#%*@@@%-:*+:-%@*. .*@@*-..:=%+==+=%@@@@@###*#+########\n###%%%%%#@@@#:-#::*%@%..+@@@%*=--+@+=**=*%@@@@@*#**#*#######\n####%%@#@@%%#-=%#%@@@@==@@@@@@@#%@@@@@#+**@@@@@%##**##**####\n#%%%@@%@@#*=%++@@@@@@@@@@@@@@@@@@@@@@@@%%*@@@@@@##**########\n%%#@@@@@%=%*@%@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@#########%#\n##%@@@@+#+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@%##%###%%##\n##%@@@@=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@#%########\n###@%%@=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%##########\n%%#@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%####%#%*##\n###%@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%%########\n###@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%##%#######\n###@%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%###########\n##%@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%#%###%###\n###@@@@#@%%@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@%%%%%#%#####\n##%@@@@@@#+@*@=#@@@%=%@@*#@@=*@@@@@@@@@@@@%@@@@@%%%%%%######\n###%@@@@@@+@=@:+%@*-:*%=:=@@==%@@##@@#*@%@@@@@@%#%%%*+######\n####%@@@@@#%+%-+%#=::+#:.-%@=:+@@+*@@%#@%@@@@@@%###%###%####\n###*#@@@@@@@*#=+%%*-:=%:.:+@=-=@#++*@%#@@@@@@@@%%##%######%#\n#####%@@@@@@@@#+@@%+=+@=::+%#*#@@%#%@@@@@@@@@@@%%##%########\n######@@@@@@@@@@@@%##%@@%%@@@@@@@@@@@@@@@@@@@@@%#%#%########\n######%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%%%%#%%%%%###\n########%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%#######%####\n#######%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%%%#%%%%###%%##\n######*##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%####\n#***#%@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%######\n*##%@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%#%%%%##\n%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%####\n%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%#")
            if fight(gnasher):
                print("The lifeless body of the gnasher lies before you")
                time.sleep(para.Swait)
                x = input("A: Consume\n B: Follow monster's trail\n C: Continue\n").lower()
                if x == "a":
                    print("You close your eyes and begin to consume the gnasher, imagining the carrion before you as something more appetizing")
                    time.sleep(para.Mwait)
                    print("Alas, no amount of fantasy can mask the foul taste that permeates your tongue")
                    time.sleep(para.Swait)
                    x = player.hunger
                    player.hunger += para.largerestore
                    if player.hunger > 100:
                        player.hunger = 100
                    print("[Hunger +"+ str(player.hunger - x)+"]")
                    player.sanity -= para.largechange
                    print("[Sanity -"+str(para.largechange)+"]")

                elif x == "b":
                    print("The gnasher's rampage may have opened up some new shortcuts")
                    time.sleep(para.Mwait)
                    print("You follow the monster's trail of destruction, hoping it can get you closer to your goal")
                    y = random.randint(0, 100) + player.luck
                    if y < 25:
                        print("The monster's path twists and turns, and you end up further from your target than when you started")
                        time.sleep(para.Swait)
                        print("[Distance -3]")
                        misc.distance -= 3

                    elif y > 75:
                        print("The gnasher's rampage has torn down walls and demolished houses, allowing new routes to open up which were previously inaccessible.")
                        time.sleep(para.Mwait)
                        print("Taking a shortcut through the ruined houses, you manage to save some time")
                        time.sleep(para.Swait)
                        print("[Distance +3]")
                        misc.distance += 3

                    else:
                        print("You follow the monster's trail for what seems like ages, but you end up back where you started.")
                        print("[Hunger -"+(para.smallchange)+"]")
                        player.hunger -= para.smallchange

class sorrowc(encounters):
    def __init__(self):
        super().__init__(10, 101, "sorrow")
    def text(self):
        print("Combat encounter: sorrow")
        print("You see a figure kneeling on the ground")
        time.sleep(para.Mwait)
        print("Their body is wrapped in chains extending out from the walls and floor")
        time.sleep(para.Mwait)
        print("Not a single part of their body is visible under the chains, save for a single eye, which locks its gaze onto you")
        time.sleep(para.Mwait)
        print("Upon noticing your presence, the entity stands up and charges at you!")
        from character_sheets import sorrow
        fight(sorrow)

class ravenc(encounters):
    def __init__(self):
        super().__init__(13, 101, "crow")
    def text(self):
        #print("can kill for 30 hunger -1 luck or evade for -10 hunger. If insane, triggers fight")
        print("You spot a raven gorging itself on a nearby carcass")
        time.sleep(para.Mwait)
        if player.sanity > 50:
            print("The sight of it reminds you of your own hunger.")
            time.sleep(para.Swait)
            print("The raven may not be the only one who gets to eat today.")
            time.sleep(para.Mwait)
            eat = input("Consume the raven?\nA: Yes\nB: No\n").lower()
            if eat == "a":
                x = random.randint(0,100)+player.luck
                if x >= 75:
                    print("You pounce on the raven, grabbing it before it has the chance to fly away")
                    time.sleep(para.Mwait)
                    print("It flaps and squabbles in your hands, but a quick bash against the wall makes it falls silent")
                    time.sleep(para.Mwait)
                    print("As you eat, you recall an old legend you once heard about the corvids")
                    time.sleep(para.Mwait)
                    print("In days of yore, the birds used to be lauded as harbingers of doom")
                    time.sleep(para.Mwait)
                    print("But that's just a myth, right?")
                    time.sleep(para.Mwait)
                    x = player.hunger
                    player.hunger += para.smallchange
                    if player.hunger > 100:
                        player.hunger = 100
                    print("[Hunger +"+str(player.hunger-x)+"]")
                    player.luck -= para.smallschange
                    print("[Luck -"+str(para.smallschange)+"]")

                else:
                    print("You lunge at the raven, but it quickly flaps out of the way, leaving your hands to grasp nothing but the cold air")
                    time.sleep(para.Mwait)
                    print("You continue to chase the raven for several more minutes, determined to catch your meal")
                    time.sleep(para.Mwait)
                    print("In the end, the raven gets tired of taunting you and flies away, leaving you exhausted and out of breath")
                    time.sleep(para.Mwait)
                    print("[Hunger -"+str(para.smallchange)+"]")
                    player.hunger -= para.smallchange
            else:
                print("It's not worth it")

        else:
            print("Suddenly the raven stops, raising its head and staring directly at you")
            time.sleep(para.Mwait)
            print("There's something cold and unnatural about the raven's gaze which sends shivers down your spine")
            time.sleep(para.Mwait)
            battle = False
            x = input("A: look closer\nB: communicate\nC: run\n").lower()
            if x == "a":
                print("You take a better look at the raven")
                time.sleep(para.Mwait)
                print("The bird stands unnaturally still, not even breathing")
                time.sleep(para.Mwait)
                print("Despite this, it's feathers and body are too detailed to call a statuette or robot")
                time.sleep(para.Mwait)
                print("But the most interesting part of the corvid, are its eyes")
                time.sleep(para.Mwait)
                print("At first they seemed to be an inky black void, completely dilated with no hint of colour in sight")
                time.sleep(para.Mwait)
                print("But upon closer inspection, you realise you can make out faint movement within the eyes")
                time.sleep(para.Mwait)
                print("Something lurks on the other side, lurking, waiting, watching you back")
                time.sleep(para.Mwait)
                print("Upon noticing it, you are hit with an overwhelming sense of humility and powerlessness")
                time.sleep(para.Swait)
                print("'Y̶̖̼̕ỏ̵̘̝u̵͓̾̎ ̸̧̰̔͘c̶͕̲̔̄a̶̼͋n̴̻̦͒͝n̴͓̼͐ó̷̥ẗ̴͎́̿ ̶͚̭̐͝s̶͙̾t̷͎̂o̸̤̽̀p̴̩̈ ̸̬͒u̶͊͜š̷͇͐'\n'R̵̝̓e̸̛̖s̷͇̾i̵̦̐s̶̻͊ẗ̴̤a̵͙̽n̵̖͒c̶̹̎ẹ̷̑ ̴̒ͅį̵̅s̷͔͝ ̴̤̀f̶̦̓ṳ̵̈́ẗ̷̘ȉ̵̫l̴̪̒e̸͚͝'\n'G̶̳̱̉͛î̴̯̈́̃v̷̱̍̂e̶̺͑̀ ̵̟͆̋͠ṷ̷̽͌̏p̵̲̽'̮\n'S̵̼̅u̵̥̕b̸͚́m̴̤̊i̴̹͋ţ̴͛'\n'Y̵̟͂o̸̻̎u̸̖͝ ̴̦͝w̶̦̾i̵͍̋ļ̴̆l̴̥̂ ̴̝͊f̵̾ͅą̶̕í̶̠l̴͔͝'\n'O̶̼̯̎͠b̴̖̋̌e̵͍̔̈́y̷̘̒'\n'O̷͙̭̝̒̄ḃ̵̮̠͇̋e̶̘̽ý̷̗͔͌'\n'O̶̻͙͑̑b̴͔͒̃̆e̸̜̬̅̄̐̎ͅy̵̝͎̏͌̌͠'")
                time.sleep(para.Lwait)
                print("You pull away, your mind reeling from the psychic attack it faced")
                print("[Sanity -"+str(para.largechange)+"]")
                player.sanity -= para.largechange
                time.sleep(para.Mwait)
                print("As you are recovering, the raven begins to step towards you, its movements jerky and mechanical like a puppet on strings")
                battle = True
            elif x == "b":
                print("You attempt to communicate with the raven")
                time.sleep(para.Mwait)
                print("Its beak does not move, yet you hear its voice. It does not speak in any language you know, yet you understand it anyway")
                time.sleep(para.Mwait)
                print("Its words inflict an overwhelming sense of powerlessness and despair onto you")
                time.sleep(para.Mwait)
                print("'T̴̺̄o̵͎͑ ̶͚̚t̷̠͈͊h̶̰̰͆͆e̷͙͓͒ ̶̙͌a̸͍̋c̸̞̉c̸̗͋͜ǔ̶̧̟r̷̭͐͒ṡ̶̭͗ë̵͇d̶̡̤̃ ̶̻͖͝f̵̢͆o̷͕̹̓o̵͂͜l̴̓ͅ,̶̟̆̓ ̶̻͂ẅ̴͍́̿h̸̪͠ȍ̶̒ͅ ̴͚̽͂s̴͍̈́ȩ̷̗̄͋e̶̞͛k̵̫̝̋͌s̵̖̔ ̶̖̔t̵̫̜̑̓o̴̘̎ ̴̹́c̷͙̞̉͑ẖ̴̜͂̑a̶̗̞͌ṅ̷̘̈g̵̡̮̋e̷̳̯͐ ̶̩̥̆͘t̸̲̰́ḧ̴̢̤e̶͓̞͋ ̵̧͎̊͝i̷̻͎̋ņ̴̉͠e̵̩͐̂ṽ̷̼i̵̧̊̈́ẗ̵̻́͌à̴͓́b̷͚̤̂̿ḷ̶͠e̴͔̩̍͗,̸̙͝ ̴̪̦͘h̵͇͑͠e̸̡̚͠e̸͚͒d̶̥͌͐ ̶̙͛m̵̮͐͌ÿ̸͓́ ̴̨̇͘w̸̠̹̿͝a̶̻̫̐r̵̳̠̔̚ń̸͖i̷͛ͅn̸̠̾̐g̸̜͐.̶̲̲̓͠ ̴̨̮͗'\n'̷͍̳͐Y̸̪͋̈́ȏ̵̺͍u̵͓̙͊͘r̷̖̻͑̿ ̷̟͊t̴͈̑ͅa̴̦̔̇s̷̨̻̾̍k̸̼̏͌ ̴̢̄ḭ̵̠̚ş̵̮̇ ̴̝̙͊s̵̱̹̆͑i̶̖̾͘s̷͖͋̈́y̵͖̎p̶̪̿̅h̶̠̜̒̂ḛ̷̽̏ȁ̴̜͖ṇ̵̼̾͘,̶̣͆ ̴͎̬̅t̶͓͉͠ḧ̷͇ę̸̨̇̋ ̵̥̖̉ñ̸̠a̷̝͜͠r̶̖̰̅r̴͓͛a̴̰̩͗̋t̷̩̂i̸̬̟̐v̴̪͛é̴̠̫̑ ̵̛͔̼u̶͉͋ṅ̷͕̉c̶̘͐h̴̦́͆ã̸̳̱n̵͖̫͒̀g̸͖̓ȅ̶̩̊ặ̷̾b̴̼̋̆l̴͎̓͐e̴͙̓.̶̢̣̃̓ ̸̠̾̚'\n'̶͓͒̃T̴̩̀̋h̴͈̖͠e̶̗͔͝ ̸͙̃̀f̶̬̩̕ỏ̷̡͍̍r̵̞͚̋̄c̵̗̾ͅȇ̴̜͗s̵̠̬̑ ̶̟̏y̴͙͐õ̵̥͓ư̷͕̥̆ ̴̺̬͒͌f̸̫̙̕a̵̰̼̋̆c̵̪̩͑e̷̮͒ ̷̘̉͜ą̶̪͊r̸̯͘e̴͇͆ ̶̻͇̍̇ǵ̷̜́r̸̨͉̈e̵̮̹̿ä̵̳̻́͘t̶͖͋ẽ̵̞͝r̶̖͚͛ ̴̭̔́t̶͇̑h̸̞̚a̷̹͘n̶̠͈̆̄ ̶̻̃̋͜ŷ̷̹̮͘o̷̥͌͂ű̵̖̜r̵̼̳̃ ̴̻̀w̸͍̌̈i̶͎̬͒l̷͕̗͐̒d̵̪̏ĕ̸̘š̸̯̟̃t̴̲̊ ̴͉̤͊͂c̸̼̆͠o̵̼̭̿͘m̸̢͋p̴͈̈̋r̷͕̆è̵͕̞h̸̠̳̕ȩ̸̼̈͑n̷̟̂̌s̷̥̘̍̎i̵̢̽o̵̡̐n̵̘̎.̵̱̂ ̵̣̳̈́'\n'̶̃͜Ţ̶͍̅̔h̴̢͚̔̕è̵͈ ̶̺̆͂p̸̬̉̇o̸͔̐̚w̸͇̗̉͠ę̴̞͘r̴̲͚͋͊ ̸͓̅ö̸̥̙́f̴͇̟̕ ̷͇̏t̷͈̽h̵̤͑̌e̵̡͍̍ ̴̫̂̚G̸͕͎̏r̶̬̻͗e̷̦͍̊͋a̷͉̋͛t̴͍͌ ̴̡̗̚Ọ̷͘l̴̼̼͝d̴̙̹̅̀ ̵̬͖̏Ȍ̴͈̫̔n̴̤͎̎ê̶̹͍͂ ̷̧͙͑͛c̴̺̈ǎ̴̼̓ņ̸̯̿͝n̷̤̹̆͒o̷̡̎t̴̮͖̊̒ ̸̟̾̄ͅb̴̙̪̄́e̴̜̼̋ ̴̳̾ŝ̶̳͉̑ẗ̷͈̅ó̴̈́͜p̸͉̲͋p̶͔̀̔e̷̠͂d̶̨̊.̴̯͊ ̸̩͒̿'\n'̶͚̒̋Y̷̫̅o̵̝̅u̸̗͊̂ ̸̡̝͂̕s̶̢͖͝h̵̖͙̆̋ą̴̆l̸̛͍̯l̷̺̼̍ ̸̗̚f̸̳͖͝a̴̲̪̐̀i̵̫͗l̷̰͗̉͜ ̷̦͇̋ị̶̰̉͝ň̵̛̻̥ ̷͙̏̉ỹ̴̱̼ỏ̷̦̥u̶̍ͅr̸͈̰̂ ̸͖̤̌q̷͉̿́ͅu̸͕̻͑ẹ̴̓̋s̶̭̑t̸͙̃,̴̠̍ ̸̹̃̿l̴̡̖̓ǐ̷̞̝͝ḵ̶̞̂͠e̵̱̠̒͘ ̶͚́̓a̴͙̚l̸̗̓l̴̝͑ ̵͙̄̚ő̵̬t̸͙͑ͅh̶͉͗͠e̷̙͛r̷̳̿̆s̵̨̮̉͌ ̷̻̣͋b̴̥̈́̀ë̸̩̯́͊f̵̖͠ô̶͙̌r̵͎̺̅͐ė̴̩ ̷̞̓̉y̷̪͕͗ǒ̷̟̓ṳ̶͒̾ͅ.̶͙͓́'")
                time.sleep(para.Lwait)
                print("After it finishes talking, the bird flies away")
                print("[Sanity -"+str(para.largechange)+"]")
                player.sanity -= para.largechange
            elif x == "c":
                print("You run as fast as you can, away from the raven")
                time.sleep(para.Mwait)
                print("You've survived long enough to know that whatever was going on couldn't be good.")
                time.sleep(para.Mwait)
                print("Still, the haunting gaze of the raven stays in your mind long after you escape it")
                time.sleep(para.Mwait)
                print("[Hunger -"+str(para.smallchange)+"]")
                print("[Sanity -"+str(para.smallchange)+"]")
                player.hunger -= para.smallchange
                player.sanity -= para.smallchange

            if battle:
                from character_sheets import raven
                if fight(raven):
                    print("The raven lies lifeless in front of you")
                    time.sleep(para.Mwait)
                    x = input("Consume the raven?\nA: Yes\nB: No\n").lower()
                    if x == "a":
                        print("You consumed the raven")
                        time.sleep(para.Swait)
                        print("Tastes like chicken")
                        time.sleep(para.Mwait)
                        h = player.hunger
                        player.hunger += para.smallrestore
                        if player.hunger > 100:
                            player.hunger = 100
                        print("Hunger +"+str(player.hunger - h)+"]")

class tunnelchasec(encounters):
    def __init__(self):
        super().__init__(15, 101, "tunnelchase")
    def text(self):
        print("You come across a tunnel which seems to have been carved out by some large creature")
        time.sleep(para.Mwait)
        print("Traveling through it could allow you to reach your destination sooner")
        time.sleep(para.Mwait)
        x = input("Take a shortcut through the tunnel?\nA: Yes\nB: No\n").lower()
        if x == "a":
            print("You step into the tunnel")
            time.sleep(para.Mwait)
            print("As you descend, the tunnel gets darker and smaller, constricting around you")
            time.sleep(para.Mwait)
            if random.randint(1, 100) + player.luck  < 75:
                print("However, as you navigate through the suffocating depths, you hear something which makes your blood freeze")
                time.sleep(para.Mwait)
                print("The sound of claws digging their way through the earth can be heard, rapidly getting louder and louder")
                time.sleep(para.Mwait)
                print("What will you do?")
                time.sleep(para.Swait)
                x = input("A: Stand and fight\nB: Run\n").lower()
                battle = False

                if x == "a":
                    print("You brace yourself as you stand your ground")
                    time.sleep(para.Mwait)
                    print("The earth shakes as a large man furiously claws his way towards you")
                    time.sleep(para.Mwait)
                    print("His face is discoloured and misshapen, and his hands have been replaced by sharp, bony shovels")
                    time.sleep(para.Mwait)
                    print("Before you know it, he stands in front of you")
                    battle = True

                else:
                    print("You desperately move yourself forwards, hoping to outrun whoever else lurks in the tunnel")
                    time.sleep(para.Mwait)
                    print("The earth shakes as you hear something rapidly moving towards you")
                    time.sleep(para.Mwait)
                    print("Up ahead, you can see a faint light, the end is in sight!")
                    if random.randint(1, 100) + player.luck <= 70:
                        print("However, your hope is dashed as your leg becomes caught in one of the tunnel's crevices, stopping you in your tracks")
                        time.sleep(para.Mwait)
                        print("You frantically try to pull your foot out, but are interrupted by a sharp blade penetrating your chest")
                        time.sleep(para.Mwait)
                        print("[Health -2]")
                        player.health -= 2
                        print("Pain shoots through your body as you turn yourself around, to face your attacker")
                        battle = True

                if battle:
                    from character_sheets import digger
                    if fight(digger):
                        print("The corpse of the moleman lies in front of you")
                        time.sleep(para.Mwait)
                        eat = input("Consume the moleman?\nA: Yes\nB: No\n").lower()
                        if eat == "a":
                            x = player.hunger
                            player.hunger += para.largerestore
                            if player.hunger > 100:
                                player.hunger = 100
                            print("[Hunger +" + str(player.hunger - x) + "]")
                            player.sanity -= para.largechange
                            print("[Sanity -" + str(para.largechange) + "]")


            if player.health > 0:
                print("You stumble out of the tunnel, having skipped past several streets")
                time.sleep(para.Swait)
                print("[Distance +3]")
                misc.distance += 3

        else:
            print("You don't want to be trapped there if the creature returns")

class lore2c(encounters):
    def __init__(self):
        super().__init__(15, 101, "lore2")
    def text(self):
        print("You find a file stuffed with papers in a nearby bin")
        time.sleep(para.Mwait)
        print("The front of the file is stamped with the words '[CONFIDENTIAL- MARKED FOR IMMEDIATE DISPOSAL]'")
        time.sleep(para.Mwait)
        x = input("Read the papers in the file?\nA: Yes\nB: No\n").lower()
        if x == "a":
            print("You take a look at the papers")
            time.sleep(para.Mwait)
            print("They appear to be a research paper on something")
            time.sleep(para.Mwait)
            print("                                                    'Report on Zathene energy and its properties'")
            time.sleep(para.Lwait)
            print("'The newly discovered Zathene energy seems to be an answer to our prayers, being a fully renewable power source able to produce trillions of gigajoules per second'")
            time.sleep(para.Mwait)
            print("'However, this is not without skepticism from some people in the general public'")
            time.sleep(para.Mwait)
            print("'Because of this, I aim to put these worries to rest by conducting a full investigation on this new power source and its effects, with the endorsement and help of Vexon Industries'")
            time.sleep(para.Mwait)
            print("\n\n'In this study I will investigate:'")
            time.sleep(para.Mwait)
            print("'1. The physical properties of Zathene energy'")
            time.sleep(para.Mwait)
            print("'2. The source of Zathene energy and where exactly it is drawn from'")
            time.sleep(para.Mwait)
            print("'3. The potential risks this new type of energy may pose'")
            time.sleep(para.Mwait)
            while True:
                contents = input("\nWhich section will you go to?\nA: Physical properties\nB: Source of energy\nC: Potential risks\nD: Stop reading\n").lower()
                if contents == "a":
                    print("'Physical properties of Zathene energy'")
                    time.sleep(para.Mwait)
                    print('"In its base form, Zathene energy exists as a plasma of positively charged particles invisible to the naked eye"')
                    time.sleep(para.Mwait)
                    print("'However, while it cannot be seen, it can still be percieved'")
                    time.sleep(para.Mwait)
                    print("'People exposed to Zathene energy in its uncatalysed state have been able to detect it, not through any known sensory organ but instead through 'their soul'")
                    time.sleep(para.Mwait)
                    print("'They have often described the feeling it causes as spiritual or mystic, speaking to them in a way which cannot be explained through science'")
                    time.sleep(para.Mwait)
                    print("'I suggest such claims should be taken critically, as all to often such 'religious phenomena' are simply the result of natural processes and human fantasy'")
                    time.sleep(para.Mwait)
                    print("\n'Its most notable property however, is its reaction once stimulated with a negative charge'")
                    time.sleep(para.Mwait)
                    print("'When the two meet, the Zathene energy will undergo an explosive reaction, rapidly heating up and taking on a bright red colouration'")
                    time.sleep(para.Mwait)
                    print("'In this form, its appearance is quite similar to that of electricity'")
                    time.sleep(para.Mwait)
                    print("'This new form is extremely charged with energy, which it will immediately try to get rid of by discharging into its surroundings'")
                    time.sleep(para.Mwait)
                    print("'By surrounding it with conductors, this energy can be harvested and transferred through the grid to use as power'")
                    time.sleep(para.Mwait)
                    print("'Whats truly amazing, is the amount of energy output far exceeds the amount of energy needed to generate negative charge for it'")
                    time.sleep(para.Mwait)
                    print("'By all accounts this should be scientifically impossible, and yet this new substance seems to have achieved it'")
                    time.sleep(para.Mwait)
                    print("'Conclusion: Further testing is required'")
                    time.sleep(para.Mwait)

                if contents == "b":
                    print("'The source of Zathene energy'")
                    time.sleep(para.Mwait)
                    print("'As was revealed to the press, Zathene energy was reportedly discovered by Vexon industries at one of their oil drilling plants off the east coast of Arkham'")
                    time.sleep(para.Mwait)
                    print("'However, what was not revealed was the form they found this energy in'")
                    time.sleep(para.Mwait)
                    print("'What Vexon industries found was not an isolated cluster of Zathene energy, but instead a large stone obelisk- which the energy surrounded'")
                    time.sleep(para.Mwait)
                    print("'What Vexon industries found was not an isolated cluster of Zathene energy, but instead a large stone obelisk- which the energy surrounded'")
                    time.sleep(para.Mwait)
                    print("'I was lucky enough to be permitted access to the obelisk in order to conduct further tests, in which I made a number of interesting discoveries.'")
                    time.sleep(para.Mwait)
                    print("'The obelisk itself is quite peculiar in appearance, containing numerous illustrations and symbols etched into it in a language I do not understand'")
                    time.sleep(para.Mwait)
                    print("'But what was even more peculiar, was what I found when I began studying it'")
                    time.sleep(para.Mwait)
                    print("'First of all, the obelisk did not attract Zathene energy like I had initially thought. Instead, it seemed to actively repel it away from itself'")
                    time.sleep(para.Mwait)
                    print("'The reason why so much Zathene energy was detected around the obelisk was instead because the obelisk appeared to be actively producing the energy and distributing it to its surroundings.'")
                    time.sleep(para.Mwait)
                    print("'This came as quite a shock to me. While Zathene energy had already displayed its exemption from the laws of conservation with its reactive properties, that was entirely different from an object of solid stone seemingly defying everything we knew about it.'")
                    time.sleep(para.Mwait)
                    print("'Luckily, Vexon Industries also lent me access to their laboratory to further study the obelisk for the rest of the month'")
                    time.sleep(para.Mwait)
                    print("'Upon studying the obelisk more thoroughly over the course of the month, I made several more interesting discoveries'")
                    time.sleep(para.Mwait)
                    print("'Namely:'")
                    time.sleep(para.Mwait)
                    print("'- While its properties may seem similar to a rock, the obelisk's atomic structure does not match any known stone or other material in our universe'")
                    time.sleep(para.Mwait)
                    print("'- Additionally, when inspecting the obelisk's surface, I discovered high quantities of dark matter clustured around it.")
                    time.sleep(para.Mwait)
                    print("\n'The presence of this unidentifiable material, the presence of dark matter on it's surface, as well as it seemingly emitting endless amounts of zathene energy have led me to believe this obelisk may be a gateway to an alternate universe'")
                    time.sleep(para.Mwait)
                    print("'For whatever reason, this obelisk appears to be a meeting point between the two worlds, leading to energy from one universe leaking out into the other'")
                    time.sleep(para.Mwait)
                    print("'This means that we should be continually supplied with energy until the other universe runs out, which will take a googol amount of years.'")
                    time.sleep(para.Mwait)
                    print("'In layman's turns, we have a practically infinite amount of energy which we can use'")
                    time.sleep(para.Mwait)
                    print("'The existence of other universes is a groundbreaking discovery, which could propel us millions of years forward in technology'")
                    time.sleep(para.Mwait)
                    print("'Further testing is highly anticipated'")
                    time.sleep(para.Mwait)
                    print("\n'Additionally over the course of my studies, I noticed that the obelisk's output of zathene energy had been gradually increasing overtime'")
                    time.sleep(para.Mwait)
                    print("\n'This is most likely not cause for concern, though I decided reported it to Vexon Industries' head supervisor as a precaution'")
                    time.sleep(para.Mwait)

                if x == "c":
                    print("'Potential risks of Zathene energy'")
                    time.sleep(para.Mwait)
                    print("'While many have been rejoicing the discovery of Zathene energy and resolution to Arkham's power crisis, other's have remained skeptical, questioning the safety of such a new and unknown power source'")
                    time.sleep(para.Mwait)
                    print("'I cannot blame them, after all, skepticism sparks research and new discoveries- which is why I decided to run some experiments on the dangers of Zathene energy myself'")
                    time.sleep(para.Mwait)
                    print("'First, I exposed 3 mice to a low dosage of zathene energy for a 24 hours'")
                    time.sleep(para.Mwait)
                    print("'When first exposed, the mice responded with fear and distress, perhaps from not knowing the cause of the spiritual sensation zathene enrgy is known to trigger'")
                    time.sleep(para.Mwait)
                    print("'By the end of the 24 hours however, the mice had returned to normal behavior, with no long-lasting changes'")
                    time.sleep(para.Mwait)
                    print("'Upon seeing this, I decided to up the dosage of zathene energy they were exposed to and return in another 24 hours'")
                    time.sleep(para.Mwait)
                    print("'This seemed to have the opposite effect. While at first, none of the mice exhibited any changes in behaviour, when I came back at the end of the day, I found 2 of the 3 mice dead, seemingly killed and eaten by the survivor.'")
                    time.sleep(para.Mwait)
                    print("'I tested by suspicions by introducing two more mice to the cage, and sure enough, the infected mouse killed both of them as soon as they entered the cage'")
                    time.sleep(para.Mwait)
                    print("'I then decided to introduce a cat into the cage. Similar to with the mice before, the infected mouse showed high levels of aggression and tried to attack the cat as soon as it was introduced'")
                    time.sleep(para.Mwait)
                    print("'Ultimately, the cat was able to kill the mouse, but not without sustaining heavy injuries'")
                    time.sleep(para.Mwait)
                    print("'Interested in seeing what could happen at even higher exposure levels, I repeated my experiment with 3 new mice, increasing the exposure to 10x the levels of before.'")
                    time.sleep(para.Mwait)
                    print("'Immediately, the mice appeared to fall under extreme pain, though I decided to once again wait the full 24 hours to see what the effects would be'")
                    time.sleep(para.Mwait)
                    print("'When I returned, I was met with a gruesome sight. One of the mice had murdered the other two, following my expectations. What I hadn't expected however, was that the zathene energy had forcibly mutated the mouse, causing several changes to occur on its body'")
                    time.sleep(para.Mwait)
                    print("''These changes were but not limited to:''")
                    time.sleep(para.Mwait)
                    print(" '- Increased size'")
                    time.sleep(para.Swait)
                    print(" '- The growth of additional rows of sharp teeth'")
                    time.sleep(para.Swait)
                    print(" '- Sharpened claws'")
                    time.sleep(para.Swait)
                    print(" '- Yellow discolouration of the eyes'")
                    time.sleep(para.Swait)
                    print(" '- Growth of additional eyes on its back and forehead'")
                    time.sleep(para.Swait)
                    print("'- Malformed snout'")
                    time.sleep(para.Swait)
                    print("'- Overproduction and build up of bodily fluids'")
                    time.sleep(para.Swait)
                    print("'- Large swelling and tumour growth all over the body'")
                    time.sleep(para.Mwait)
                    print("\n'The mouse also displayed even higher levels of aggression than before, even trying to attack me through the glass window in its enclosure'")
                    time.sleep(para.Mwait)
                    print("'Thankfully, as the glass was bulletproof, it was not able to succeed, and I was able to euthanise the creature by flooding its cage with carbon monoxide'")
                    time.sleep(para.Mwait)
                    print("\n'In conclusion, while seemingly harmless in small doses, prolonged exposure to large doses of zathene energy appear to cause extreme amounts of aggression in the individual, and even mutating them if the dosage is high enough'")
                    time.sleep(para.Mwait)
                    print("'However, as the experiment was only conducted on mice, it is currently unknown if the same results could apply to larger animals such as humans'")
                    time.sleep(para.Mwait)
                    print("'Overall, I would suggest to exercise caution around the implementation of zathene energy, and will be reporting my findings to the head of Vexon Industries'")

                elif contents == "d":
                    print("Research papers are boring")

class stalkerc(encounters):
    def __init__(self):
        super().__init__(15, 101, "stalker")
    def text(self):
        from parameters import stalking
        stalking.switch = True
        stalking.text[stalking.counter]()

# class beelzebubc(encounters):
#     def __init__(self):
#         super().__init__(15, 50, "beelzebub")
#     def text(self):
#         print("Combat encounter: glutton")

class blackcatc(encounters):
    def __init__(self):
        super().__init__(15, 101, "blackcat")
    def text(self):
        print("eat cat to lose sanity for hunger or pet cat for luck decrease")
        print("If sanity is low and pet cat, fight cheshire")

class restc(encounters):
    def __init__(self):
        super().__init__(15, 101, "rest")
    def goodsleep(self):
        print("You instantly fall asleep, ridding yourself of all the exhaustion acquired on your adventure")
        time.sleep(para.Mwait)
        print("When you wake up, you feel reinvigorated and ready to take on the world")
        time.sleep(para.Mwait)
        z = player.sanity
        player.health = player.maxhealth
        player.sanity += para.smallchange
        if player.sanity > 100:
            player.sanity = 100
        player.hunger -= para.smallchange
        print("[Health fully restored]")
        print("[Sanity +"+str(player.sanity-z))
        print("[Hunger -"+str(para.smallchange)+"]")

    def badsleep(self):
        print("You find yourself tossing and turning throughout the night, unable to stay asleep")
        time.sleep(para.Mwait)
        print("Still, any amount of rest is better than nothing")
        time.sleep(para.Mwait)
        y = player.health
        player.health += (player.maxhealth/2)
        if player.health > player.maxhealth:
            player.health = player.maxhealth
        player.hunger -= para.smallchange
        print("[Health +"+str(player.health - y)+"]")
        print("[Hunger -"+str(para.smallchange)+"]")

    def attacked(self):
        print("You are suddenly awoken by the feeling of a large blunt object slamming into your ribs")
        print("[Health - 1]")
        player.health -= 1
        time.sleep(para.Mwait)
        print("Shooting up, you realise you are surrounded by two masked men")
        time.sleep(para.Mwait)
        print("They must have snuck up on you while you were asleep!")
        time.sleep(para.Mwait)
        from character_sheets import batter
        fight(batter)
        print("The second masked man attacks!")
        time.sleep(para.Mwait)
        fight(batter)

    def robbed(self):
        print("You sleep soundly through the night")
        time.sleep(para.Mwait)
        z = player.sanity
        player.health = player.maxhealth
        player.sanity += para.smallchange
        if player.sanity > 100:
            player.sanity = 100
        player.hunger -= para.smallchange
        print("[Health fully restored]")
        print("[Sanity +" + str(player.sanity - z)+"]")
        print("[Hunger -" + str(para.smallchange) + "]")
        time.sleep(para.Mwait)
        print("However upon waking up, you realise that someone had gone through your items while you were asleep!")
        if player.gold > 0:
            print("They stole 1 gold!")
            time.sleep(para.Swait)
            print("[Gold -1]")
            player.gold -= 1
        else:
            from invmenu import words
            hasitems = False
            for i in range(len(words)):
                if player.inv[words[i]] > 0:
                    print("They stole 1", words[i]+"!")
                    player.inv[words[i]] -= 1
                    hasitems = True
                    break

            if hasitems == False:
                print("However, as you had no items to steal, they seem to have left you alone")

    def nightmare(self):
        print("Suddenly, you find yourself in an unfamiliar world")
        time.sleep(para.Mwait)
        print("You are standing in the middle of a barren desert which stretches out for miles.")
        time.sleep(para.Mwait)
        print("When you look up there is no sky, only the endless void of space")
        time.sleep(para.Mwait)
        print("You spot what seems to be a temple in the distance, the only landmark in an otherwise empty world")
        time.sleep(para.Mwait)
        print("As you walk towards it, you feel a sense of tranquility, as though all of your worries are leaving you behind")
        time.sleep(para.Mwait)
        print("That is, until you reach the walls of the temple and take a closer look")
        time.sleep(para.Mwait)
        print("Rows upon rows of flesh, gasping and squirming in unison, make up the walls of the temple")
        time.sleep(para.Mwait)
        print("They cry out in pain, but nobody is there to hear them")
        time.sleep(para.Mwait)
        print("You wake up from your nightmare, gasping for breath")
        time.sleep(para.Mwait)
        print("Will this be your fate if Zath-Kopchyla is summoned?")
        time.sleep(para.Mwait)
        y = player.health
        player.health += (player.maxhealth / 2)
        if player.health > player.maxhealth:
            player.health = player.maxhealth
        player.hunger -= para.smallchange
        player.sanity -= 30
        print("[Health +" + str(player.health - y) + "]")
        print("[Hunger -" + str(para.smallchange) + "]")
        print("[Sanity-30]")

    def visitor(self):

        def visit1():
            print("Not wanting to view whatever horror may lie before you, you keep your eyes tightly shut")
            time.sleep(para.Mwait)
            print("The monster speaks again, this time with more agitation in it's voice")
            time.sleep(para.Mwait)
            print("O̴̘͒p̶̮̀e̴͉͆ǹ̴̨ ̸͖̒y̶̕͜ö̷̥u̸̳͝r̸͈̚ ̵͓̾e̶̪͑y̷̛͍e̵̠̐ș̷̾!̵̼̑")

        def visit2():
            print("You shut your eyes tighter, refusing to yield to the creature's will")
            time.sleep(para.Mwait)
            print("Suddenly, you feel a clawed hand wrap around your throat")
            time.sleep(para.Mwait)
            print("Ö̸̝́P̸̀ͅĘ̷̽N̶̟̾ ̸̤̆Y̷͍͒O̵͖̔U̶̝̚R̴̡͛ ̸̟̓Ē̵̜Y̴̛̫Ë̵̻́S̵̹̀")

        def visit3():
            print("The creature's claws begin to dig into your throat")
            time.sleep(para.Swait)
            print("[Health -1]")
            player.health -= 1
            time.sleep(para.Mwait)
            print("You hear the monster screaming now")
            time.sleep(para.Mwait)
            print("Ọ̸͛Ṕ̶̞E̶̞͛N̸̖͠ ̶̜̀Ỹ̶̠O̸̯̿U̶͉̍R̸͎̒ ̵̭̂Ȇ̴̜Y̷͇͛Ḛ̶̊S̵͕̀!̸͍͘")

        def visit4():
            print("You feel the monster clawing its way through your flesh, screaming at the top of its lungs")
            time.sleep(para.Mwait)
            print("Ọ̸͛Ṕ̶̞E̶̞͛N̸̖͠ ̶̜̀Ỹ̶̠O̸̯̿U̶͉̍R̸͎̒ ̵̭̂Ȇ̴̜Y̷͇͛Ḛ̶̊S̵͕̀!̸͍͘")
            time.sleep(para.Mwait)
            print("[Health -2]")
            player.health -= 2

        print("Suddenly, you hear a voice beside you")
        time.sleep(para.Mwait)
        print("ǫ̴̅p̵̙̑ȩ̷̍n̷̍͜ ̶͎̕y̵͉͝ȯ̷̢u̶̳͛r̶̙̾ ̶̩̌ẹ̶͠y̷̳̕e̶̗͝s̶͎͗")
        time.sleep(para.Mwait)
        print("The voice is low and raspy, with murderous intent")
        demon = [visit1, visit2, visit3, visit4]
        count = 0
        while player.health > 0:
            open = input("Open your eyes?\nA: Open\nB: Keep shut\n").lower()
            if open == "b":
                if count >= 3:
                    demon[3]()
                else:
                    demon[count]()

                count +=1

            else:
                print("Preparing for the worst, you open your eyes")
                time.sleep(para.Mwait)
                print("However when you do, there is no monster standing next to you")
                time.sleep(para.Mwait)
                print("The room is empty, save for you and the crackling fire")
                time.sleep(para.Mwait)
                print("[Sanity -"+str(para.smallchange)+"]")
                player.sanity -= para.smallchange
                break

        if player.health <= 0:
            print("Suddenly, the monster's shouting stops")
            time.sleep(para.Mwait)
            print("As does the pain of it digging into your chest")
            time.sleep(para.Mwait)
            print("As does your thoughts")
            time.sleep(para.Mwait)
            print("You have perished")



    def text(self):
        # print("Come to place to rest")
        # print("A: press on at sanity decrease")
        # print("B sleep")
        # print("When sleeping one of several events will happen:")
        # print("A: All health and sanity is restored")
        # print("B: health and sanity is partially restored")
        # print("C: You are attacked while sleeping and take first hit, starting consecutive fight")
        # print("D: If sanity is low you are visited by an entity who tells you to open your eyes. You will take damage until you do. If you do open them, nothing will be there and you lose sanity")
        # print("E: If Doom is high enough you will be taken to the Elder God's domain for a nightmare. Significant sanity decrease and partial health increase")
        # print("F: You will have your stuff stolen, remove one item from inventory")

        print("After walking for a while, you find a closed-off area with a campfire beside it")
        time.sleep(para.Mwait)
        print("It has been too long since you last got any sleep, and it has taken it's toll on you")
        time.sleep(para.Mwait)
        x = input("Rest here?\nA: Yes\nB: No\n").lower()
        if x == "a":
            print("You lie by the fire and close your eyes for a brief moment")
            dreams = [self.goodsleep, self.badsleep, self.attacked, self.robbed, self.nightmare, self.visitor]
            time.sleep(para.Mwait)
            if player.sanity < 50:
                sleep = random.randint(0, 5)

            else:
                sleep = random.randint(0, 4)

            dreams[sleep]()

        else:
            print("It's too risky")
            time.sleep(para.Mwait)
            print("Ignoring the weight of your eyelids, you drearily trudge onwards")
            time.sleep(para.Swait)
            print("[Sanity -"+str(para.smallchange)+"]")
            player.sanity -= para.smallchange

class muggingc(encounters):
    def __init__(self):
        super().__init__(15, 101, "mugging")
    def text(self):
       # print("Give all money or fight 3 consecutive masked men")
        print("You find the way forwards blocked off by 3 masked men, all wielding baseball bats")
        time.sleep(para.Mwait)
        print("One of them notices you and steps forward")
        time.sleep(para.Mwait)
        print("'Hey You!'")
        time.sleep(para.Swait)
        print("'Not sure if you've noticed, but this place is our territory now'")
        time.sleep(para.Mwait)
        print("'Don't worry, we're not gonna hurt you- provided you exactly what we say'")
        time.sleep(para.Mwait)
        print("'Now... Hand over all your gold and we'll let you pass through here unscathed'")
        time.sleep(para.Mwait)
        brawl = False
        betray = False
        if player.gold <= 0:
            print("'You don't have enough gold?'")
            time.sleep(para.Mwait)
            print("'Well then, I suppose you'll just have to give us everything you DO have!")
            time.sleep(para.Mwait)
            from invmenu import words
            hasitems = False
            for i in range(len(words)):
                if player.inv[words[i]] > 0:
                    hasitems = True
            if hasitems == False:
                print("You're really telling me ya don't have ANYTHING on you?")
                time.sleep(para.Mwait)
                print("'That's fine, there's still one other way you can pay us...'")
                time.sleep(para.Mwait)
                print("'With your life!'")
                brawl = True
            else:
                gift = input("Hand over your items?\nA: Yes\nB: No way!\n").lower()
                if gift == "a":
                    print("You give up all your items to the masked gang")
                    time.sleep(para.Swait)
                    player.inv["meat"] = 0
                    player.inv["pills"] = 0
                    player.inv["bandages"] = 0
                    player.inv["charm"] = 0
                    player.inv["steroids"] = 0
                    time.sleep(para.Mwait)
                    print("[All items lost]")
                    betray = True
                else:
                    print("'Then I'll just have to pry em from your cold, dead hands!'")
                    brawl = True
        else:
            x = input("A: Hand over all gold\nB: Refuse\nC: Find another way forwards\n").lower()
            if x == "a":
                print("You gave all your gold to the masked gang")
                time.sleep(para.Swait)
                print("[All gold lost]")
                player.gold = 0
                betray = True

            elif x == "c":
                print("You go to turn around, but are suddenly restrained by two of the masked men!")
                time.sleep(para.Mwait)
                print("'Oh I don't think so, we aren't letting you go that easily!'")
                time.sleep(para.Mwait)
                print("You struggle with all your might")
                time.sleep(para.Swait)
                if random.randint(1, 100) + player.luck < 50:
                    print("However, your captor's grip is too strong, and you are unable to escape")
                    time.sleep(para.Mwait)
                    print("Your struggling is quickly by the swift blow of a baseball bat to your legs ")
                    time.sleep(para.Mwait)
                    print("[Health -1]")
                    player.health -= 1
                    time.sleep(para.Swait)
                    print("You are released onto the floor as the three thugs gather around you")
                    time.sleep(para.Mwait)
                    print("'C'mon, get up'")
                    time.sleep(para.Swait)
                    print("'This party's just getting started!'")
                    brawl = True
                else:
                    print("and you manage to break free from their grasp!")
                    time.sleep(para.Mwait)
                    print("You dash down the streets, with the masked bandits hot on your tail")
                    time.sleep(para.Mwait)
                    print("You run and run until your legs cannot hold you anymore, and you collapse onto the streets")
                    time.sleep(para.Mwait)
                    print("Your pursuers are nowhere to be found")
                    time.sleep(para.Mwait)
                    print("[Hunger -"+str(para.largechange)+"]")
                    print("[Distance -5]")
                    player.hunger -= para.largechange
                    misc.distance -= 5

            else:
                print("'Aww, look at that'")
                time.sleep(para.Swait)
                print("'This one must have a death wish!'")
                time.sleep(para.Mwait)
                print("'C'mon boys, let's help the poor thing get exactly what it needs'")
                brawl = True

        if brawl == True:
            from character_sheets import batter
            fight(batter)
            print("The second masked man attacks!")
            fight(batter)
            print("'Oh no ya don't!'")
            time.sleep(para.Swait)
            print("The third masked man attacks!")
            fight(batter)

        if betray == True:
            print("You pass on through, now with considerably lighter pockets than before")




class mansionc(encounters):
    def __init__(self):
        super().__init__(15, 101, "mansion")
    def text(self):
        print("Stay at creepy guy's mansion")

class doctorc(encounters):
    def __init__(self):
        super().__init__(16, 101, "doctor")
    def text(self):
        print("You encounter a man in a bloodstained doctor's uniform")
        time.sleep(para.Mwait)
        print(
            "He shambles towards you, pulling down his mask to reveal a crooked row of yellow teeth fixed in a menacing grin")
        time.sleep(para.Mwait)
        print("'Ah, a healthy donor! It's been so long since I've had someone like you.'")
        time.sleep(para.Mwait)
        print(
            "'Please, won't you consider donating your blood for those in need? There are many dying patients who could use it much more than you, and I'll offer a reward too!'")
        time.sleep(para.Mwait)
        print("The doctor raises a long rusted needle, covered in bits of dried blood")
        time.sleep(para.Mwait)
        print("Accept the", "doctor's", "request?")
        time.sleep(para.Swait)
        print("A: Yes")
        print("B: No way!")
        x = input()
        x = x.lower()
        if x == "a":
            print("The doctor jabs the needle into your arm with the care and grace of an enraged bull")
            time.sleep(para.Mwait)
            print(
                "Blood spurts out of your arm with vigor, as the doctor produces a bottle and flails around trying to catch it all")
            time.sleep(para.Mwait)
            print(
                "The sight and amount of  blood leaving your body makes you dizzy, and you find yourself losing consciousness")
            time.sleep(para.Mwait)
            print("[Health -" + str(para.largeschange) + "]")
            time.sleep(para.Mwait)
            print("When you come to, the doctor stands before you, an empty bottle clutched in his hands")
            time.sleep(para.Mwait)
            print(
                "'Well unfortunately we were not able to collect much blood this time round, but a deal is a deal so I shall give you your compensation'")
            time.sleep(para.Mwait)
            print("The doctor bends over and hands you 2 gold")
            time.sleep(para.Mwait)
            print("You see a red liquid trickle down the corner of the doctor's mouth, which he quickly licks up")
            time.sleep(para.Mwait)
            print(
                "Anyway, I hope you come again, many patients are counting on your blood, we simply MUST have it!")

        else:
            print("You turn to leave, you already have yourself to worry about")
            time.sleep(para.Mwait)
            print("Suddenly, your arm is grasped by the doctor's!")
            time.sleep(para.Mwait)
            print("'Oh I don't think so. Your blood is simply to precious for us to give up!'")
            time.sleep(para.Mwait)
            if random.randint(0, 100) + player.luck + player.atk > 55:
                print("You manage to pull free of the mad doctor's grasp and escape")
            else:
                print("combat encounter: doctor")

class sacrificec(encounters):
    def __init__(self):
        super().__init__(16, 101, "sacrifice")
    def text(self):
        print("Sacrifice health for statboost/lower doom")

class witchc(encounters):
    def __init__(self):
        super().__init__(16, 101, "witch")
    def text(self):
        print("Offered a potion which will restore/harm or raise/lower a stat")

class cultc(encounters):
    def __init__(self):
        super().__init__(17, 101, "cult")
    def text(self):
        print("Perform ritual with cult to raise doom or fight members consecutively")
        print("If doom is high, cultists get a stat increase")

class altarc(encounters):
    def __init__(self):
        super().__init__(17, 101, "altar")
    def text(self):
        print("You come across a mysterious altar")
        time.sleep(para.Mwait)
        print("You hear voices calling to you, inviting you to join them")
        time.sleep(para.Lwait)
        if player.luck+random.randint(0,100) > 75 == True:
            print()
            print("You resist the voices and press on")
        else:
            print()
            print("Your mind wavers, as you feel yourself losing your grip on reality")
            time.sleep(para.Swait)
            print("[Sanity -30]")
            player.sanity -= 30

class crawlerc(encounters):
    def __init__(self):
        super().__init__(17, 101, "crawler")
    def text(self):
        print("Combat encounter: crawler")

class mirrorc(encounters):
    def __init__(self):
        super().__init__(20, 101, "mirror")
    def text(self):
        print("You look in the mirror")
        time.sleep(para.Mwait)
        if player.sanity < 50:
            print("insane encounter: mimic")
        elif player.luck+random.randint(0,100) > 30 == True:
            print("It's you")
        else:
            print("That's not you")
            time.sleep(para.Swait)
            print("[Sanity -" + str(para.v.smallchange) + "]")
            player.sanity -= para.v.smallchange

class hunterc(encounters):
    def __init__(self):
        super().__init__(20, 101, "hunter")
    def text(self):
        print("Combat encounter: hunter")

class mimicc(encounters):
    def __init__(self):
        super().__init__(17, 101, "mimic")
    def text(self):
        print("Combat encounter: mimic")

class lore3c(encounters):
    def __init__(self):
        super().__init__(20, 101, "lore3")
    def text(self):
        print("cult room")

class trapc(encounters):
    def __init__(self):
        super().__init__(25, 101, "trap")
    def text(self):
        print("Chance for item or take damage")

class fleshortcutc(encounters):
    def __init__(self):
        super().__init__(25, 101, "fleshortcut")
    def text(self):
        print("fleshortcut")

class amigarac(encounters):
    def __init__(self):
        super().__init__(30, 101, "amigara")
    def text(self):
        print("go through crack, gain distance but lose health, max sanity and hunger to 50 and gain attack")

class holesc(encounters):
    def __init__(self):
        super().__init__(30, 101, "holes")
    def text(selfr):
        print("Sees holes on hand, can either cut it out and take damage, or let holes spread for reduced max hp")

class saviorc(encounters):
    def __init__(self):
        super().__init__(30, 101, "savior")
    def text(self):
        print("Fight consecutive battles and be rewarded or ignore at sanity cost")

class amalgamc(encounters):
    def __init__(self):
        super().__init__(35, 101, "amalgam")
    def text(self):
        print("Combat encounter: Amalgam")

class angelc(encounters):
    def __init__(self):
        super().__init__(35, 50, "angel")
    def text(self):
        print("Combat encounter: Angel")

class gods_callingc(encounters):
    def __init__(self):
        super().__init__(35, 50, "gods_calling")
    def text(self):
        print("You hear the voices of the old ones calling to you")
        time.sleep(para.Mwait)
        x = para.Lwait
        for i in range(50):
            print("S̷̗̪̆͗U̷͓̚͝F̷̲̒F̷̩͕̄̕Ḙ̷̡͠R̶͖̂ ̸̹̗̂F̷̮̦͝O̷̰̎R̴̡̖̃ ̴̳̓̓Ṁ̴̹͍E̷̠͌ͅ")
            time.sleep(x)
            x /= para.Mwait
        t_end = time.time() + 1
        while time.time() < t_end:
            print("S̷̗̪̆͗U̷͓̚͝F̷̲̒F̷̩͕̄̕Ḙ̷̡͠R̶͖̂ ̸̹̗̂F̷̮̦͝O̷̰̎R̴̡̖̃ ̴̳̓̓Ṁ̴̹͍E̷̠͌ͅ")
        if random.randint(0,100)+ player.luck > 75:
            print("You cast  them out of your head and press on")
            time.sleep(para.Mwait)
            print("You won't let them try to control you anymore")
            time.sleep(para.Mwait)
            print("Sanity fully restored")
            Sanity = 100
        else:
            print("You shakily draw a knife and plunge it into your stomach")
            time.sleep(para.Mwait)
            print("[Health -" + str(player.atk) + "]")
            player.health -= player.atk

class maskedbasec(encounters):
    def __init__(self):
        super().__init__(40, 101, "masked base")
    def text(self):
        print("Can either sneak by, steal food or turn back")
        print("stealing food has higher chance of failure, turning back results in loss of distance")
        print("if caught, fight 2 masked men and then leader")

class terrorc(encounters):
    def __init__(self):
        super().__init__(40, 50, "terror")
    def text(self):
        print("Combat encounter: Terror")

class dollc(encounters):
    def __init__(self):
        super().__init__(40, 101, "doll")
    def text(self):
        print("Combat encounter: doll")

class hydrac(encounters):
    def __init__(self):
        super().__init__(40, 101, "hydra")
    def text(self):
        print("Combat encounter: Hydra")

class skinwalkerc(encounters):
    def __init__(self):
        super().__init__(40, 101, "skinwalker")
    def text(self):
        print("Combat encounter: skinwalker")

class HADc(encounters):
    def __init__(self):
        super().__init__(40, 101, "H.A.D")
    def text(self):
        print("Combat encounter: H.A.D")


def stalk5():
    print("You feel like someone is right behind you")
    time.sleep(para.Mwait)
    x = input("Turn around?\nA: Yes\nB: No\n").lower()
    if x == "a":
        print("You turn around")
        time.sleep(para.Mwait)
        if random.randint(1, 100) + player.luck < 50:
            print("But there was no-one there")
            time.sleep(para.Swait)
            print("[Sanity -= 20]")
            player.sanity -= 20
            stalking.counter = 3
        else:
            print("You see a all man clutching a knife in his hands grinning back at you")
            from character_sheets import stalker
            if fight(stalker):
                x = input("The corpse of the stalker lies in front of you\nA: Consume\nB: Leave\n").lower()
                if x == "a":
                    print("Unfortunately, there is not much meat on his bones, but you take what you can get")
                    time.sleep(para.Mwait)
                    x = player.hunger
                    player.hunger += para.smallrestore
                    if player.hunger > 100:
                        player.hunger = 100
                    print("[Hunger +" + str(player.hunger - x) + "]")
                    player.sanity -= para.largechange
                    print("[Sanity -" + str(para.largechange) + "]")

            stalking.counter = 0
            stalking.switch = False
    else:
        print("You're probably just imagining it, right?")
        time.sleep(para.Swait)
        print("[Sanity -20]")
        player.sanity -= 20
        stalking.counter = 3


flavour = flavourc()
Nsaneflavour = Nsaneflavourc()
eldritchvisions = eldritchvisionsc()
foodfind = foodfindc()
pillfind = pillfindc()
bandagefind = bandagefindc()
goldfind = goldfindc()
itemfind = itemfindc()
stargaze = stargazec()
slime = slimec()
zombie = zombiec()
shadow = shadowc()
lootcorpse = lootcorpsec()
lore1 = lore1c()
shrine = shrinec()
konami = konamic()
drink = drinkc()
deersac = deersacc()
batter = batterc()
shop = shopc()
gnasher = gnasherc()
sorrow = sorrowc()
raven = ravenc()
tunnelchase = tunnelchasec()
lore2 = lore2c()
stalker = stalkerc()
blackcat = blackcatc()
rest = restc()
mugging = muggingc()
mansion = mansionc()
doctor = doctorc()
sacrifice = sacrificec()
witch = witchc()
cult = cultc()
altar = altarc()
crawler = crawlerc()
mirror = mirrorc()
hunter = hunterc()
mimic = mimicc()
lore3 = lore3c()
trap = trapc()
fleshortcut = fleshortcutc()
amigara = amigarac()
holes = holesc()
savior = saviorc()
amalgam = amalgamc()
angel = angelc()
gods_calling = gods_callingc()
maskedbase = maskedbasec()
terror = terrorc()
doll = dollc()
hydra = hydrac()
skinwalker = skinwalkerc()
HAD = HADc()

#encounters = different events which can occur
eventable = [flavour, Nsaneflavour, eldritchvisions, foodfind, bandagefind, pillfind, goldfind, itemfind, stargaze, slime, zombie, shadow, lootcorpse, lore1, shrine, konami, deersac, drink, batter, gnasher, sorrow, tunnelchase, shop, lore2, raven, stalker,  blackcat, rest, mugging, mansion, doctor, sacrifice, cult, altar, fleshortcut, hunter, crawler, mirror, mimic, witch, lore3, trap, amigara, amalgam, angel, gods_calling, maskedbase, terror, savior, doll, hydra, skinwalker, HAD]
last = ""

from parameters import stalking
def encounterpick(event):
    validevents = []
    if stalking.counter > 3:
        stalk5()
    for i in range(len(eventable)):
        if misc.difficulty >= eventable[i].diff and player.sanity <= eventable[i].san and eventable[i] != event:
            validevents.append(eventable[i])
    event = validevents[random.randint(0, len(validevents) - 1)]
    event.text()
    return (event)
#