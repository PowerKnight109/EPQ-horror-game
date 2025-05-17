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
        print("insane event")


class foodfindc(encounters):
    def __init__(self):
        super().__init__(1, 101, "meat")
    def text(self):
        print("You found some meat!")
        player.inv["meat"] +=1

class pillfindc(encounters):
    def __init__(self):
        super().__init__(99, 101, "Nsaneflavour")
    def text(self):
        print("You found some pills!")
        player.inv["pills"] += 1

class bandagefindc(encounters):
    def __init__(self):
        super().__init__(99, 101, "bandages")
    def text(self):
        print("You found some bandages!")
        player.inv["bandages"] += 1

class goldfindc(encounters):
    def __init__(self):
        super().__init__(1, 101, "goldfind")
    def text(self):
        print("You found some gold!")
        player.gold += 1

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
        print("A slime drips down")
        from character_sheets import slime
        time.sleep(para.Mwait)
        print(".................................................................\n...........................::::--:::.............................\n.........................::*#%%%##%#=::..........................\n................:::...::=#%%%%%%%%%%%%@%=:::.....................\n.............::::+#*-=*#%%#%%#%%%%%%%%%%%%*:.::::::..............\n..........:-*####%%%%%%##%%%%%%%%%%%%%%%%%%%%#%%##%*:............\n.........:+%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#:...........\n.........:*%%%%%%%%%#%%%%%%%%%%%####%%%@@@%%%%%%%%%%%=:..........\n.........:#%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*#%%%%%%%%%%#%#-:........\n.......::*%%%%%%%%%%%%%%%%%%%%%%%%%%+-::::::-#%@%%%%%%%#-........\n......:=#%%%%%%%%%###%%%%%%%%%%%%%%-::::+##*::+%@%%%%%%%%:.......\n......-#%%##%%%%%%%%%%%%%%%%%%%%%%*::::-@@@@@::%%%%%@%%%%:.......\n.....:%%%%%%%%%%#%%%%%%%%%%%%%%%%%@:::::::+-:::*@%%#%%%%%-.......\n....:*%%%%%%%%%%%@%%%@@%##%%%%%##%@%=::::::::::%@%%%#%%%%*::::...\n....-#%%%%%##%%#-::::-==#%%%%%%%%%%%%+=::::::-#@%%%%%@%%%%*......\n...:+%%%%@%%%%-+%#=:::=#@%%%%%%%%%%%%%##****%@@#%%#%%%%%%%%-.....\n...:*%%#%%%%#--@@@+-+@@%@%%%%%%%%%%%%%%%%%%%%%%#%%%%%#%%%%%+::::.\n...:#%#%%%#%#+=+*#%%@%%%%%%%%%%%%%%%%%%%%%%%%%%%#%%%%#%%%%%-::::.\n...:*%%%%%%%%@@@%%%%@%%%%%%%%%%%%%%#%%%%%%%%%%%%##%%##%%%%%:.....\n...:*%%%%%%#%%%%%%%%%%%%%%%##%%%%%=-#%#=*%%%%%%%%%%%%%%%%%*:::...\n...:*%%%%%%%%%%%%%%%%%%%%%--+%=#%*--+*--=%+#%%%%%%%%%%%%%%=......\n...:=%%%%%%%%%%%%%%%#+%+*+---*-=%+--+%=-*%-+%*%%%%%%%@%%%#-......\n....:%%%%%%%%%%%%%%%--=------*%%%%%%%%%%%%%%%%%%%%%%%%%%%*:......\n....:#%%%%%@%%%%%%=%**#%%%%%%#--%#%%%%--*@#%%%%%%%%%%%%%%*:......\n....:*%%%%%+%%%%%%%%-%+-#+#%%=----#@*%=*%%%%%%###%%%%%%%%*:......\n....:-@%%%+:-#%%%%%%%%+-=+*%%%#%%#%%%%%%%%%%%%%%%%%*+%%%%*:......\n.....:#%%#:..:*%%%%%%%%+%%%%%%%%%%%%%%%%%%%%%%%%%%=::#%%%+:......\n.....:=%%*::..::+%%%%%#%%%%%%%%%#%%%%%#%%%%%%%%%#-::::%%%=.......\n......-%%+:......:+%%%%%%%%%%%%%%@%%%%%%%%%%%*%%::...:+%%=.......\n.....::#%+:.......::+%%%%%%%%=%%%@%%%%%%%%#+*%%=::...:=%%-.......\n......:+%*:.........:+#-:*%%%-%%%*+%+::#*:..:#%:.....:=%%=:......")
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
            print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@........@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@............@@.....@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@................@@.......@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@............@@@@.............@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@....@....@@@@@@@@@@....@@.........@@@@@@@@@@...@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@.......@@@@@@@@@@@@@@@@@...@@......@@@@@@@@@@@@@@@..@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@......@@@@@@@@@@@@@@@@@@@............@@@@@@@@@@@@@@@@@@..@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@.....@@@@@@@@@@@@@.....@@@............@@@@@@@@@@@@@@@@@@@@...@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@....@@@@@@@@@@@@@...@@..@@.........@@@@@@@@@@@@.....@@@@@@@@....@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@...@@@@@@@@@@@@@@......@@.............@@@..@@@@..@@..@@@@@@@@.....@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@..@@@@@@@@@@@@@@@@@@@@@..................@@@.@@@....@@@@@@@@@@@......@@@@@@@@@@@@@@@@@\n@@@@@@@@@...@@@@@@@@@@@@@@@..........................@@@..@@@@@@@@@@@@@@@.......@@@@@@@@@@@@@@@@\n@@@@@@@@.@@@@@........@@@..............................@@@@.....@@@@@@@@@@@......@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@.......@@@@.....@@@@.......................@@...............@@@......@@@@@@@@@@@@@@\n@@@@@@@@...........@@...@@@@@..........................@@..................@@@....@@@@@@@@@@@@@@\n@@@@@@@................@@@............................@.....................@@@....@@@@@@@@@@@@@\n@@@@@@...............@@@..........................@@@@....................@@@@.....@@@@@@@@@@@@@\n@@@@@@..............@@...........................@@@@@@...............@@@@@@@@.....@@@@@@@@@@@@@\n@@@@..............@@@@......@@..................@@@@@@@@@@...........@@@@@@@@@.....@@@@@@@@@@@@@\n@@@................@@@@....@@@@@@@@............@@@@@@@@@@@@..........@@@@@@@@@.........@@@@@@@@@\n@@@@@@..............@@...@@@@@@@@@@@@@@@@@..@@@@@@@@@@@@@@@@@.......@@@@@@@@@@........@@@@@@@@@@\n@@....@.............@@..@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@....@@@..@@@@@@@@\n@@....@............@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..@@.....@@@@@@@\n@@....@...........@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.@......@@@@@@@\n@@@...@@.........@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.....@@@@@@@@\n@@@.....@@@.....@@@@@...@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@......@@@@@@@@\n@@@@.......@@@@@@@@@.......@@@@@@@@@@@@@@@@@@@@@@@@@@@@@......@@@@@@@@@@@@@@@@@@@@.....@@@@@@@@@\n@@@@@......@@@@@@@@...........@@@@@@@@@@@@@@@@@@@@@@@@............@@@@@@@@@@@@@@@@....@@@@@@@@@@\n@@@@@@....@@@....................@@@@@@@@@@@@@@@@@@..................@@@@@@@@@@@@.....@@@@@@@@@@\n@@@@@@@@@.@@@......................@@@@@@@@@@@@@......................@@@@@@@@@@@....@@@@@@@@@@@\n@@@@@@@@@@@@..........................@@@@@@@@........................@@...@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@.............................@@@@........................@@@.....@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@............................@@@.........................@@@........@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@...........................@@@@@....................@@@@@@.......@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@............................@@@@@@.................@@@@@.....@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@...........................@@@@@...............@@@@@@.@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@.......................@@@@@................@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@.................@@@@@@.................@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@............@@@@@@@................@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@...........@@@@@@@@...........@@.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@...@@@......@@@@@@@@......@@........@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@........@@....@@@@@@@@.@@............@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@..............@@@@@@@@@@...............@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@........................................@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@..........................................@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
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
        print("....................................................................................................\n....................................................................................................\n....................................................................................................\n....................................................................................................\n....................................................................................................\n....................................................................................................\n....................................................................................................\n.............................................@@@@@@@@@@.............................................\n.......................................@@@@@@@@......@@@@@@@@.......................................\n.....................................@@@....................@@@.....................................\n....................................@..........................@....................................\n...................................@.........@@......@@@........@...................................\n..................................@.......@@@@@.......@@@@.......@..................................\n..................................@.......@@............@@.......@..................................\n..................................@..............................@..................................\n..................................@..............................@..................................\n..................................@..............................@..................................\n..................................@..............................@..................................\n..................................@..@@....................@@....@..................................\n..................................@...@@@@@@@@@@@@@@@@@@@@@@.....@..................................\n..................................@.......@@@@@@@@@@@@@@@........@..................................\n...................................@........@@@@@@@@@@@@........@...................................\n....................................@@@......................@@@....................................\n........................................@@@@.............@@@@.......................................\n.............................................@@@@@@@@@@@@...........................................\n............................................@...........@...........................................\n............................................@...........@...........................................\n..........................................@@............@@..........................................\n......................................@@@@................@@@@......................................\n...............................@@@@@@@@......................@@@@@@@@...............................\n..........................@@@@@@....................................@@@@@@..........................\n.......................@@@@..............................................@@@@.......................\n.....................@@@....................................................@@@.....................\n....................@@@......................................................@@@....................\n...................@@@........................................................@@@...................")

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
                    print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@........@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@............@@.....@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@................@@.......@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@............@@@@.............@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@....@....@@@@@@@@@@....@@.........@@@@@@@@@@...@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@.......@@@@@@@@@@@@@@@@@...@@......@@@@@@@@@@@@@@@..@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@......@@@@@@@@@@@@@@@@@@@............@@@@@@@@@@@@@@@@@@..@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@.....@@@@@@@@@@@@@.....@@@............@@@@@@@@@@@@@@@@@@@@...@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@....@@@@@@@@@@@@@...@@..@@.........@@@@@@@@@@@@.....@@@@@@@@....@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@...@@@@@@@@@@@@@@......@@.............@@@..@@@@..@@..@@@@@@@@.....@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@..@@@@@@@@@@@@@@@@@@@@@..................@@@.@@@....@@@@@@@@@@@......@@@@@@@@@@@@@@@@@\n@@@@@@@@@...@@@@@@@@@@@@@@@..........................@@@..@@@@@@@@@@@@@@@.......@@@@@@@@@@@@@@@@\n@@@@@@@@.@@@@@........@@@..............................@@@@.....@@@@@@@@@@@......@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@.......@@@@.....@@@@.......................@@...............@@@......@@@@@@@@@@@@@@\n@@@@@@@@...........@@...@@@@@..........................@@..................@@@....@@@@@@@@@@@@@@\n@@@@@@@................@@@............................@.....................@@@....@@@@@@@@@@@@@\n@@@@@@...............@@@..........................@@@@....................@@@@.....@@@@@@@@@@@@@\n@@@@@@..............@@...........................@@@@@@...............@@@@@@@@.....@@@@@@@@@@@@@\n@@@@..............@@@@......@@..................@@@@@@@@@@...........@@@@@@@@@.....@@@@@@@@@@@@@\n@@@................@@@@....@@@@@@@@............@@@@@@@@@@@@..........@@@@@@@@@.........@@@@@@@@@\n@@@@@@..............@@...@@@@@@@@@@@@@@@@@..@@@@@@@@@@@@@@@@@.......@@@@@@@@@@........@@@@@@@@@@\n@@....@.............@@..@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@....@@@..@@@@@@@@\n@@....@............@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..@@.....@@@@@@@\n@@....@...........@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.@......@@@@@@@\n@@@...@@.........@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.....@@@@@@@@\n@@@.....@@@.....@@@@@...@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@......@@@@@@@@\n@@@@.......@@@@@@@@@.......@@@@@@@@@@@@@@@@@@@@@@@@@@@@@......@@@@@@@@@@@@@@@@@@@@.....@@@@@@@@@\n@@@@@......@@@@@@@@...........@@@@@@@@@@@@@@@@@@@@@@@@............@@@@@@@@@@@@@@@@....@@@@@@@@@@\n@@@@@@....@@@....................@@@@@@@@@@@@@@@@@@..................@@@@@@@@@@@@.....@@@@@@@@@@\n@@@@@@@@@.@@@......................@@@@@@@@@@@@@......................@@@@@@@@@@@....@@@@@@@@@@@\n@@@@@@@@@@@@..........................@@@@@@@@........................@@...@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@.............................@@@@........................@@@.....@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@............................@@@.........................@@@........@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@...........................@@@@@....................@@@@@@.......@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@............................@@@@@@.................@@@@@.....@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@...........................@@@@@...............@@@@@@.@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@.......................@@@@@................@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@.................@@@@@@.................@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@............@@@@@@@................@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@...........@@@@@@@@...........@@.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@...@@@......@@@@@@@@......@@........@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@........@@....@@@@@@@@.@@............@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@..............@@@@@@@@@@...............@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@........................................@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@..........................................@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
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
        print("lore1: paper about energy in sea")

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
                print("How much food will you offer?")
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
        x = input("A: Complete the sacrifice\nB: Consume\n C: Free the deer\n").lower()
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
            print("..@@@@@@....@.@@@@@@...........@@......................@@@@@....@..@@...........\n.....@@......@@@@@.......................................@@@@@..................\n........@...@@@@@.........................................@@@@@.....@........@@.\n...........@@@@@............................................@@@@@...@....@@.@@..\n..........@@@@@..............................................@@@@@....@@.@@.....\n.........@@@@@.......................................@........@@@@@@@@@@........\n.........@@@@....................................@@@@@.........@@@@@............\n........@@@@.......@@@@@.......................@@@@@@@@.........@@@@@...........\n........@@@.......@@@@@@@......................@@@@@@@@.@........@@@@...........\n.......@@@@.......@@@@@@@@@...................@@@@@@@@@@@.......................\n.......@@@@......@@@@@@@@@@@..................@@@@@@@@@@@.........@.@@@.........\n.......@..........@@@@@@@@@@..................@@@@@@@@@@@.......@.@.............\n.@.@@@@..........@@@@@@@@@@@..................@@@@@@@@@@@.........@..@@.........\n.@@@@..@.........@@@@@@@@@@@@.................@@@@@@@@@@@.........@@@@@........@\n.@@@@.@@@........@@@@@@@@@@@@.................@@@@@@@@@...........@@@@@@.....@@@\n.@@@@.@@@@@.......@@@@@@@@@@@.................@@@@@@@@.@@.........@@@@@@...@@@..\n..@@..@@@@@........@@@@@@@@@@.........@.......@@@@@@@.........@@..@@@@@..@@@....\n.@@@@..@@@@........@..@@@@@@@.....@@@@@@.@@.....@@@@@@.......@...@@@@@@@@@.....@\n.@@@@@.@@@@...........@.@@@......@@@@@@@@@.@................@@@@.@@@@@@@@....@..\n..@@@@.@@@@..@@.................@@@@@@@@@@@@@....@@........@@@@@@@@@@@@.@.......\n.@@@@@.@@@@.@@@@@.......@@@@....@@@@@@@@@@@@....@@@@.........@@@.@@@@@@@@@......\n.@@@@...@@@@.@@@..@......@@@.....@@@@@@@@@@@......@...@@@@...@@..@@@@.@@@@@.....\n.@@@@@.@@@@@.@@....@@.....@........@@@@@@@........@.@@@.....@@@.@@@@..@...@@@@@@\n.@@@@@.@.@@@@@@@...@@@@@............................@.....@@@@@@@@@@..@...@.....\n..@@@@@@.@@@@@@@@......@.@@@@@@.........@@@@@@@@.........@@@@@@@@@@@@@@.@.@.....\n..@@@@.@.@@@@@@@@@@@.........@@.@@@@@@@@@...............@@.@@..@@@@@.....@.@@@..\n..@@@@.@.@@@@@@@@@@@..................@...............@@@...@.@@@@@..........@.@\n.@@@@@@..@@@@@.@@..@@@@.............................@@@@..@..@@@@@.............\n...@@@@@@..@@@@@.@..@@@@@........................@.@@@@...@..@@@@.@.............\n...@.........@@@@.......@@@@.@.......@@@@......@@@@@@.....@.@@@@@.@.............\n....@@.@.......@@@.......@@@@@@@@@@@@@@@@@@@@@@@@@@......@...@@@@...............\n................@@@.@........@@@@@@@@@@@@...@@........@......@@@@...............\n................@@@@.@@.@....................................@@@@...............\n................@@@@@..@.@..........................@@........@@................\n..........@......@@@@@@.@.@..@..........@...@....@@@..........@@................\n.................@@@@@......@@@@@@@@@@@........@@.............@.................\n........@@@@......@.@@@.........@@@.@@@@@@@@....................................\n.....................@@.........................................................\n......................@@........................................................\n.......................@@.......................................................\n................................................................................\n................................................................................")
            from character_sheets import batter
            if fight(batter) == False:
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
        print("A: shop\nB: leave")
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
                    print("YoU DoN't HaVe EnOuGhH!")
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
            if random.randint(0, 100) + player.luck > 20:
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


        if combat == True:
            from character_sheets import gnasher
            fight(gnasher)

class sorrowc(encounters):
    def __init__(self):
        super().__init__(10, 101, "sorrow")
    def text(self):
        print("Combat encounter: sorrow")

class crowc(encounters):
    def __init__(self):
        super().__init__(13, 101, "crow")
    def text(self):
        print("Combat encounter: crow")

class tunnelchasec(encounters):
    def __init__(self):
        super().__init__(15, 101, "tunnelchase")
    def text(self):
        print("Combat encounter: digger")

class lore2c(encounters):
    def __init__(self):
        super().__init__(15, 101, "lore2")
    def text(self):
        print("Scientist research paper")

class stalkerc(encounters):
    def __init__(self):
        super().__init__(15, 101, "tunnelchase")
    def text(self):
        print("Combat encounter: stalker")

class beelzebubc(encounters):
    def __init__(self):
        super().__init__(15, 50, "beelzebub")
    def text(self):
        print("Combat encounter: glutton")

class blackcatc(encounters):
    def __init__(self):
        super().__init__(15, 101, "blackcat")
    def text(self):
        print("eat cat to lose sanity for hunger or pet cat for luck decrease")
        print("If sanity is low and pet cat, fight cheshire")

class restc(encounters):
    def __init__(self):
        super().__init__(15, 101, "rest")
    def text(self):
        print("Come to place to rest")
        print("A: press on at sanity decrease")
        print("B sleep")
        print("When sleeping one of several events will happen:")
        print("A: All health and sanity is restored")
        print("B: health and sanity is partially restored")
        print("C: You are attacked while sleeping and take first hit, starting consecutive fight")
        print("D: If sanity is low you are visited by an entity who tells you to open your eyes. You will take damage until you do. If you do open them, nothing will be there and you lose sanity")
        print("E: If Doom is high enough you will be taken to the Elder God's domain for a nightmare. Significant sanity decrease and partial health increase")
        print("F: You will have your stuff stolen, remove one item from inventory")

class muggingc(encounters):
    def __init__(self):
        super().__init__(15, 101, "mugging")
    def text(self):
        print("Give all money or fight 3 consecutive masked men")

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
            if random.randint(0, 100) + player.luck + player.strength > 55:
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


flavour = flavourc()
Nsaneflavour = Nsaneflavourc()
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
crow = crowc()
tunnelchase = tunnelchasec()
lore2 = lore2c()
stalker = stalkerc()
beelzebub = beelzebubc()
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
eventable = [flavour, Nsaneflavour, foodfind, bandagefind, pillfind, goldfind, itemfind, stargaze, slime, zombie, shadow, lootcorpse, lore1, shrine, konami, deersac, drink, batter, gnasher, sorrow,tunnelchase, shop, lore2, crow, stalker, beelzebub, blackcat, rest, mugging, mansion, doctor, sacrifice, cult, altar, fleshortcut, hunter, crawler, mirror, mimic, witch, lore3, trap, amigara, amalgam, angel, gods_calling, maskedbase, terror, savior, doll, hydra, skinwalker, HAD]
last = ""

def encounterpick(event):
    validevents = []
    for i in range(len(eventable)):
        if misc.difficulty >= eventable[i].diff and player.sanity <= eventable[i].san and eventable[i] != event:
            validevents.append(eventable[i])
    event = validevents[random.randint(0, len(validevents) - 1)]
    event.text()
    return (event)
#