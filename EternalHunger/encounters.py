from character_sheets import player, zombie, slime, shadow, batter, sorrow, gnasher, stalker, digger, raven, skinwalker, doctor, mimic, hunter, butcher
from parameters import para, misc, stalking
import time
import random
from combat import fight
from invmenu import words

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
        super().__init__(0, 101, "flavour")
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
        super().__init__(1, 50, "eldritch visions")
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

# class foodfindc(encounters):
#     def __init__(self):
#         super().__init__(1, 101, "meat")
#     def text(self):
#         print("You found some meat!")
#         player.inv["meat"] += (1+player.luck)
#
# class pillfindc(encounters):
#     def __init__(self):
#         super().__init__(1, 101, "pillfind")
#     def text(self):
#         print("You found some pills!")
#         player.inv["pills"] += 1
#
#
# class bandagefindc(encounters):
#     def __init__(self):
#         super().__init__(1, 101, "bandages")
#     def text(self):
#         print("You found some bandages!")
#         player.inv["bandages"] += 1

class essentialsc(encounters):
    def __init__(self):
        super().__init__(1, 101, "essentials")
    def text(self):
        essentials = ["meat", "pills", "bandages"]
        x = random.randint(0, 2)
        print("You found some", essentials[x]+"!")
        player.inv[essentials[x]] += 1



class goldfindc(encounters):
    def __init__(self):
        super().__init__(1, 101, "goldfind")
    def text(self):
        print("You found some gold!")
        player.gold += (1)

class itemfindc(encounters):
    def __init__(self):
        super().__init__(1, 101, "itemfind")
    def text(self):
        new = random.randint(0, len(words) - 5)
        print("You found some", words[new])
        player.inv[words[new]] += 1

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
            print("You attack the monster!")
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
            if fight(zombie) == True:
                zombie.health = zombie.maxhealth
                x = input("The unmoving body of the husk lies before you\nA: Consume\nB: Loot\nC: Leave\n").lower()
                if x == "c":
                    print("You move on")
                else:
                    if random.randint(1,100)+player.luck > 20:
                        if x == "b":
                            print("You loot the body for supplies")
                            time.sleep(para.Mwait)
                            new = random.randint(0, len(words)-1)
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
                            player.hunger += para.largerestore
                            print("[Hunger restored by", str(para.largerestore) + "]\n")
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
            if random.randint(1, 100) + player.luck > 30 - (misc.difficulty / 10):
                if choice == "a":
                    print("You loot the corpse for items")
                    time.sleep(para.Mwait)
                    new = random.randint(0, len(words)-1)
                    print("You found some", words[new])
                    player.inv[words[new]] +=1
                    # time.sleep(para.Mwait)
                    # print("You can't get the image of their lifeless face out of your head")
                    # time.sleep(para.Mwait)
                    # print("[Sanity -"+str(para.smallchange)+"]")
                    # player.sanity -= para.smallchange

                elif choice == "b":
                    print("Are you really going to resort to cannibalism?")
                    time.sleep(para.Mwait)
                    print("Well, you can't be picky in this world")
                    time.sleep(para.Mwait)
                    print("You close you eyes and sink your teeth in, forcing each bite down your throat")
                    time.sleep(para.Mwait)
                    x = player.hunger
                    player.hunger += para.largerestore
                    print("[Hunger +"+str(player.hunger - x)+"]")
                    print("[Sanity -"+str(para.largechange)+"]")
                    player.sanity -= para.largechange
            else:
                print("The corpse got up and attacked!")
                if misc.difficulty < 35:
                    #print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@........@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@............@@.....@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@................@@.......@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@............@@@@.............@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@....@....@@@@@@@@@@....@@.........@@@@@@@@@@...@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@.......@@@@@@@@@@@@@@@@@...@@......@@@@@@@@@@@@@@@..@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@......@@@@@@@@@@@@@@@@@@@............@@@@@@@@@@@@@@@@@@..@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@.....@@@@@@@@@@@@@.....@@@............@@@@@@@@@@@@@@@@@@@@...@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@....@@@@@@@@@@@@@...@@..@@.........@@@@@@@@@@@@.....@@@@@@@@....@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@...@@@@@@@@@@@@@@......@@.............@@@..@@@@..@@..@@@@@@@@.....@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@..@@@@@@@@@@@@@@@@@@@@@..................@@@.@@@....@@@@@@@@@@@......@@@@@@@@@@@@@@@@@\n@@@@@@@@@...@@@@@@@@@@@@@@@..........................@@@..@@@@@@@@@@@@@@@.......@@@@@@@@@@@@@@@@\n@@@@@@@@.@@@@@........@@@..............................@@@@.....@@@@@@@@@@@......@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@.......@@@@.....@@@@.......................@@...............@@@......@@@@@@@@@@@@@@\n@@@@@@@@...........@@...@@@@@..........................@@..................@@@....@@@@@@@@@@@@@@\n@@@@@@@................@@@............................@.....................@@@....@@@@@@@@@@@@@\n@@@@@@...............@@@..........................@@@@....................@@@@.....@@@@@@@@@@@@@\n@@@@@@..............@@...........................@@@@@@...............@@@@@@@@.....@@@@@@@@@@@@@\n@@@@..............@@@@......@@..................@@@@@@@@@@...........@@@@@@@@@.....@@@@@@@@@@@@@\n@@@................@@@@....@@@@@@@@............@@@@@@@@@@@@..........@@@@@@@@@.........@@@@@@@@@\n@@@@@@..............@@...@@@@@@@@@@@@@@@@@..@@@@@@@@@@@@@@@@@.......@@@@@@@@@@........@@@@@@@@@@\n@@....@.............@@..@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@....@@@..@@@@@@@@\n@@....@............@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..@@.....@@@@@@@\n@@....@...........@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.@......@@@@@@@\n@@@...@@.........@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.....@@@@@@@@\n@@@.....@@@.....@@@@@...@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@......@@@@@@@@\n@@@@.......@@@@@@@@@.......@@@@@@@@@@@@@@@@@@@@@@@@@@@@@......@@@@@@@@@@@@@@@@@@@@.....@@@@@@@@@\n@@@@@......@@@@@@@@...........@@@@@@@@@@@@@@@@@@@@@@@@............@@@@@@@@@@@@@@@@....@@@@@@@@@@\n@@@@@@....@@@....................@@@@@@@@@@@@@@@@@@..................@@@@@@@@@@@@.....@@@@@@@@@@\n@@@@@@@@@.@@@......................@@@@@@@@@@@@@......................@@@@@@@@@@@....@@@@@@@@@@@\n@@@@@@@@@@@@..........................@@@@@@@@........................@@...@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@.............................@@@@........................@@@.....@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@............................@@@.........................@@@........@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@...........................@@@@@....................@@@@@@.......@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@............................@@@@@@.................@@@@@.....@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@...........................@@@@@...............@@@@@@.@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@.......................@@@@@................@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@.................@@@@@@.................@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@............@@@@@@@................@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@...........@@@@@@@@...........@@.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@...@@@......@@@@@@@@......@@........@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@........@@....@@@@@@@@.@@............@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@..............@@@@@@@@@@...............@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@........................................@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@..........................................@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                    fight(zombie)
                    zombie.health = zombie.maxhealth
                else:
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
            #time.sleep(para.Mwait)
            print("'For all to long now, Arkham City has been plagued by a looming issue hanging over all our heads'")
            #time.sleep(para.Mwait)
            print("'One that, in spite of our best scientist's work, has continued to evade us, as we draw ever closer to certain doom.'")
           # time.sleep(para.Mwait)
            print("'I am of course talking about the Great Energy Crisis, and our city's struggle to find new energy sources to sustain itself, while our remaining stores rapidly wither away.'")
           # time.sleep(para.Mwait)
            print("'While we were thought to run out in 50 years, worry not! Vexon Industries, a superpower in the oil drilling industry claims that it has uncovered a new, renewable source of energy which can last us for generations!'")
            #time.sleep(para.Mwait)
            print("'This new type of energy, which they have dubbed 'zathene energy' was discovered in one of their plants off the east coast, and is reportedly 'fully renewable', producing 'trillions of gigajoules of energy per second'")
            #time.sleep(para.Mwait)
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
            if player.inv["meat"] > 0:
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
        super().__init__(3, 101, "konami")
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
                print("[Health +1]")
                player.sanity += para.smallchange
                player.health += para.smallhprestore
            else:
                print("The faucet turns on, but it doesn't produce water")
                time.sleep(para.Mwait)
                print("Instead, blood flows down, coating your hands and feet")
                time.sleep(para.Mwait)
                print("[Sanity -" + str(para.smallchange) + "]")
                player.sanity -= para.smallchange
        else:
            print("You decide to ignore it, the water isn't safe.")
            #time.sleep(para.Mwait)
            # print("But your thirst has become dire, and you find yourself growing weaker because of it")
            # time.sleep(para.Mwait)
            # print("[Health -" + str(para.smallschange) + "]")
            # player.health -= para.smallschange

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
            print("[Hunger +", str(para.smallrestore) + "]")
            print("[Sanity -"+str(para.smallchange)+"]")
            player.sanity -= para.smallchange
            player.hunger += para.smallrestore

        elif x == "c":
            print("You undo the baby deer's bindings and let it walk free")
            time.sleep(para.Mwait)
            print("It soothes your heart that something so innocent could exist in a world so cruel")
            time.sleep(para.Swait)
            print("[Sanity +"+str(para.largechange)+"]")
            player.sanity += para.largechange

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
            if fight(batter) == True:
                batter.health = batter.maxhealth
                x = input("The corpse of the masked man lies before you\nA: consume\nB: loot\nC: leave\n").lower()
                if x == "c":
                    print("You proceed forwards")
                else:
                    if random.randint(1, 100) + player.luck > 5:
                        if x == "b":
                            print("You loot the corpse for supplies")
                            from invmenu import words
                            time.sleep(para.Mwait)
                            new = random.randint(0, len(words)-1)
                            print("You found some", words[new])
                            player.inv[words[new]] += 1

                        elif x == "a":
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
                            player.hunger += para.largerestore
                            print("[Hunger restored by", str(para.largerestore) + "]")
                            print("[Sanity -30]")
                            player.sanity -= 30

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
        print("'PlEaSsSse, FeEl FrEe To BrOwSe My WaReSsS!'")
        time.sleep(para.Swait)
        print("A: Shop\nB: Leave\n")
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
                prices = [1, 2, 2, 0, 5]
                if browse in words and prices[words.index(browse)] > player.gold:
                    print("YoU DoN't HaVe EnOuGhH!")
                    time.sleep(para.Lwait)
                    #print("ThInK yOu CaN cHeAt MeEe? YoUu lAcK tHe CoInN!!!" )
                elif browse in words:
                    print("You purchased the", browse)
                    print("[Gold -"+str(prices[words.index(browse)])+"]")
                    time.sleep(para.Mwait)
                    player.gold -= prices[words.index(browse)]
                    player.inv[browse] += 1
                else:
                    break

        print("CoMe AgAiNn SsOoNn!")

class gnasherc(encounters):
    def __init__(self):
        super().__init__(10, 101, "gnasher")
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

                elif throw == "b":
                    from invmenu import words
                    while True:
                        hasitems = False
                        for i in range(len(words)):
                            if player.inv[words[i]] > 0:
                                print(words[i] + ":", player.inv[words[i]])
                                hasitems = True

                        if hasitems == True:
                            garbage = input("Type the name of the item you want to throw\n").lower
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
                    break

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
            if fight(gnasher):
                print("The lifeless body of the gnasher lies before you")
                time.sleep(para.Swait)
                x = input("A: Consume\nB: Follow monster's trail\nC: Continue\n").lower()
                if x == "a":
                    print("You close your eyes and begin to consume the gnasher, imagining the carrion before you as something more appetizing")
                    time.sleep(para.Mwait)
                    print("Alas, no amount of fantasy can mask the foul taste that permeates your tongue")
                    time.sleep(para.Swait)
                    player.hunger += para.largerestore
                    print("[Hunger +"+ str(para.largerestore)+"]")
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
                        print("[Hunger -"+str(para.smallchange)+"]")
                        player.hunger -= para.smallchange

class sorrowc(encounters):
    def __init__(self):
        super().__init__(15, 101, "sorrow")
    def text(self):
        print("You see a figure kneeling on the ground")
        time.sleep(para.Mwait)
        print("Their body is wrapped in chains extending out from the walls and floor")
        time.sleep(para.Mwait)
        print("Not a single part of their body is visible under the chains, save for a single eye, which locks its gaze onto you")
        time.sleep(para.Mwait)
        print("Upon noticing your presence, the entity stands up and charges at you!")
        fight(sorrow)

class ravenc(encounters):
    def __init__(self):
        super().__init__(13, 101, "raven")
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
                    print("[Hunger +"+str(para.smallrestore)+"]")
                    player.hunger += para.smallrestore
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
                if fight(raven):
                    print("The raven lies lifeless in front of you")
                    time.sleep(para.Mwait)
                    x = input("Consume the raven?\nA: Yes\nB: No\n").lower()
                    if x == "a":
                        print("You consumed the raven")
                        time.sleep(para.Swait)
                        print("Tastes like chicken")
                        time.sleep(para.Mwait)
                        print("Hunger +"+str(para.smallrestore)+"]")
                        player.hunger += para.smallrestore

class butchershopc(encounters):
    def __init__(self):
        super().__init__(7, 101, "butchershop")
    def text(self):
        print("You find an old, decrepit butcher's shop which you decide to take refuge in.")
        time.sleep(para.Mwait)
        print("Upon entering, you are greeted by a woman sitting at the front counter")
        time.sleep(para.Mwait)
        print("Her face is covered in rags that have been sewn over her head, and she is dressed in a bloodstained white coat and apron")
        time.sleep(para.Mwait)
        print("She doesn't seem hostile, but there's something offputting about her smile...")
        time.sleep(para.Lwait)
        print("\n'Greetings! ^q^ My name's Yi Xi, what can I do for you today?'")
        time.sleep(para.Mwait)
        while True:
            package = input("\nA: Shop\nB: Observe\nC: Leave\n").lower()
            if package == "a":
                while True:
                    print("You have", player.gold, "gold")
                    for i in range(10):
                        print("meat(1G)")
                    deli = input("type the name of the item you would like to purchase\n").lower()
                    if deli == "meat":
                        if player.gold > 0:
                            print("Hope you enjoy! ^q^")
                            print("[meat +1]")
                            time.sleep(para.Mwait)
                            player.inv["meat"] += 1
                            misc.credit += 1
                            player.gold -= 1
                        else:
                            print("骗子! You think you can try to cheat me?")
                            time.sleep(para.Lwait)
                            misc.credit -= 1
                    else:
                        break

            elif package == "b":
                yixi_affection = ["The butcher stares at you hungrily\nYou feel like you're in danger", "You notice the butcher is drooling at the mouth, despite her best attempts to hide it", "The butcher sharpens a particularly large knife\nThe sight of it fills you with unease", "The butcher doesnt seem to stare at you as hungrily as before", "The butcher gives you a friendly smile\nIt seems like you have become a valued customer"]
                if misc.credit > 4:
                    print(yixi_affection[4])
                elif misc.credit < 0:
                    print(yixi_affection[0])
                else:
                    print(yixi_affection[misc.credit])
                time.sleep(para.Lwait)
            elif package == "c":
                print("You turn to leave")
                time.sleep(para.Mwait)
                if random.randint(0,100) + player.luck + (misc.credit*10) >= 50:
                    print("'谢谢, come again soon!'")
                else:
                    print("'Oh you're not going anywhere'")
                    time.sleep(para.Mwait)
                    print("The butcher exits the counter and slowly approaches you")
                    time.sleep(para.Mwait)
                    print("I can't just let a prime cut of meat go to waste!")
                    if fight(butcher):
                        cycle = input("The carcass of the butcher lies on the floor of the shop\nA: Consume\nB: Loot\nC: Leave\n").lower()
                        if cycle == "a":
                            print("While you don't want to desecrate a carcass, you also don't want to let the offal go to waste")
                            time.sleep(para.Mwait)
                            print("Your desire is bottomless, and you end up eating until you get sick")
                            time.sleep(para.Mwait)
                            print("[Sanity -"+str(para.largechange)+"]")
                            print("[Hunger fully restored]")
                            player.sanity -= para.largechange
                            player.hunger = 100

                        elif cycle == "b":
                            print("You loot the butcher's store")
                            time.sleep(para.Lwait)
                            print("[Gold+3]\n[Meat+2]")
                            player.gold += 3
                            player.meat += 4
                break

class tunnelchasec(encounters):
    def __init__(self):
        super().__init__(17, 101, "tunnelchase")
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
                    if fight(digger):
                        print("The corpse of the moleman lies in front of you")
                        time.sleep(para.Mwait)
                        eat = input("Consume the moleman?\nA: Yes\nB: No\n").lower()
                        if eat == "a":
                            print("[Hunger +" + str(para.largerestore) + "]")
                            player.hunger += para.largerestore
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
                   # time.sleep(para.Mwait)
                    print('"In its base form, Zathene energy exists as a plasma of positively charged particles invisible to the naked eye"')
                    #time.sleep(para.Mwait)
                    print("'However, while it cannot be seen, it can still be percieved'")
                    #time.sleep(para.Mwait)
                    print("'People exposed to Zathene energy in its uncatalysed state have been able to detect it, not through any known sensory organ but instead through 'their soul'")
                   # time.sleep(para.Mwait)
                    print("'They have often described the feeling it causes as spiritual or mystic, speaking to them in a way which cannot be explained through science'")
                   # time.sleep(para.Mwait)
                    print("'I suggest such claims should be taken critically, as all to often such 'religious phenomena' are simply the result of natural processes and human fantasy'")
                   # time.sleep(para.Mwait)
                    print("\n'Its most notable property however, is its reaction once stimulated with a negative charge'")
                    #time.sleep(para.Mwait)
                    print("'When the two meet, the Zathene energy will undergo an explosive reaction, rapidly heating up and taking on a bright purple colouration'")
                    #time.sleep(para.Mwait)
                    print("'In this form, its appearance is quite similar to that of electricity'")
                   # time.sleep(para.Mwait)
                    print("'This new form is extremely charged with energy, which it will immediately try to get rid of by discharging into its surroundings'")
                 #   time.sleep(para.Mwait)
                    print("'By surrounding it with conductors, this energy can be harvested and transferred through the grid to use as power'")
                #    time.sleep(para.Mwait)
                    print("'Whats truly amazing, is the amount of energy output far exceeds the amount of energy needed to generate negative charge for it'")
                 #   time.sleep(para.Mwait)
                    print("'By all accounts this should be scientifically impossible, and yet this new substance seems to have achieved it'")
                  #  time.sleep(para.Mwait)
                    print("'Conclusion: Further testing is required'")
                   # time.sleep(para.Mwait)

                if contents == "b":
                    print("'The source of Zathene energy'")
                 #   time.sleep(para.Mwait)
                    print("'As was revealed to the press, Zathene energy was reportedly discovered by Vexon industries at one of their oil drilling plants off the east coast of Arkham'")
                 #   time.sleep(para.Mwait)
                    print("'However, what was not revealed was the form they found this energy in'")
                #    time.sleep(para.Mwait)
                    print("'What Vexon industries found was not an isolated cluster of Zathene energy, but instead a large stone obelisk- which the energy surrounded'")
               #     time.sleep(para.Mwait)
                    print("'What Vexon industries found was not an isolated cluster of Zathene energy, but instead a large stone obelisk- which the energy surrounded'")
                  #  time.sleep(para.Mwait)
                    print("'I was lucky enough to be permitted access to the obelisk in order to conduct further tests, in which I made a number of interesting discoveries.'")
                   # time.sleep(para.Mwait)
                    print("'The obelisk itself is quite peculiar in appearance, containing numerous illustrations and symbols etched into it in a language I do not understand'")
                    #time.sleep(para.Mwait)
                    print("'But what was even more peculiar, was what I found when I began studying it'")
                 #   time.sleep(para.Mwait)
                    print("'First of all, the obelisk did not attract Zathene energy like I had initially thought. Instead, it seemed to actively repel it away from itself'")
                  #  time.sleep(para.Mwait)
                    print("'The reason why so much Zathene energy was detected around the obelisk was instead because the obelisk appeared to be actively producing the energy and distributing it to its surroundings.'")
                   # time.sleep(para.Mwait)
                    print("'This came as quite a shock to me. While Zathene energy had already displayed its exemption from the laws of conservation with its reactive properties, that was entirely different from an object of solid stone seemingly defying everything we knew about it.'")
                    #time.sleep(para.Mwait)
                    print("'Luckily, Vexon Industries also lent me access to their laboratory to further study the obelisk for the rest of the month'")
         #           time.sleep(para.Mwait)
                    print("'Upon studying the obelisk more thoroughly over the course of the month, I made several more interesting discoveries'")
          #          time.sleep(para.Mwait)
                    print("'Namely:'")
           #         time.sleep(para.Mwait)
                    print("'- While its properties may seem similar to a rock, the obelisk's atomic structure does not match any known stone or other material in our universe'")
            #        time.sleep(para.Mwait)
                    print("'- Additionally, when inspecting the obelisk's surface, I discovered high quantities of dark matter clustured around it.")
             #       time.sleep(para.Mwait)
                    print("\n'The presence of this unidentifiable material, the presence of dark matter on it's surface, as well as it seemingly emitting endless amounts of zathene energy have led me to believe this obelisk may be a gateway to an alternate universe'")
              #      time.sleep(para.Mwait)
                    print("'For whatever reason, this obelisk appears to be a meeting point between the two worlds, leading to energy from one universe leaking out into the other'")
               #     time.sleep(para.Mwait)
                    print("'This means that we should be continually supplied with energy until the other universe runs out, which will take a googol amount of years.'")
                #    time.sleep(para.Mwait)
                    print("'In layman's turns, we have a practically infinite amount of energy which we can use'")
                 #   time.sleep(para.Mwait)
                    print("'The existence of other universes is a groundbreaking discovery, which could propel us millions of years forward in technology'")
                  #  time.sleep(para.Mwait)
                    print("'Further testing is highly anticipated'")
                   # time.sleep(para.Mwait)
                    print("\n'Additionally over the course of my studies, I noticed that the obelisk's output of zathene energy had been gradually increasing overtime'")
                    #time.sleep(para.Mwait)
                    print("\n'This is most likely not cause for concern, though I decided reported it to Vexon Industries' head supervisor as a precaution'")
                   # time.sleep(para.Mwait)

                if contents == "c":
                    print("'Potential risks of Zathene energy'")
#                    time.sleep(para.Mwait)
                    print("'While many have been rejoicing the discovery of Zathene energy and resolution to Arkham's power crisis, other's have remained skeptical, questioning the safety of such a new and unknown power source'")
 #                   time.sleep(para.Mwait)
                    print("'I cannot blame them, after all, skepticism sparks research and new discoveries- which is why I decided to run some experiments on the dangers of Zathene energy myself'")
  #                  time.sleep(para.Mwait)
                    print("'First, I exposed 3 mice to a low dosage of zathene energy for a 24 hours'")
   #                 time.sleep(para.Mwait)
                    print("'When first exposed, the mice responded with fear and distress, perhaps from not knowing the cause of the spiritual sensation zathene enrgy is known to trigger'")
    #                time.sleep(para.Mwait)
                    print("'By the end of the 24 hours however, the mice had returned to normal behavior, with no long-lasting changes'")
     #               time.sleep(para.Mwait)
                    print("'Upon seeing this, I decided to up the dosage of zathene energy they were exposed to and return in another 24 hours'")
      #              time.sleep(para.Mwait)
                    print("'This seemed to have the opposite effect. While at first, none of the mice exhibited any changes in behaviour, when I came back at the end of the day, I found 2 of the 3 mice dead, seemingly killed and eaten by the survivor.'")
       #             time.sleep(para.Mwait)
                    print("'I tested by suspicions by introducing two more mice to the cage, and sure enough, the infected mouse killed both of them as soon as they entered the cage'")
        #            time.sleep(para.Mwait)
                    print("'I then decided to introduce a cat into the cage. Similar to with the mice before, the infected mouse showed high levels of aggression and tried to attack the cat as soon as it was introduced'")
         #           time.sleep(para.Mwait)
                    print("'Ultimately, the cat was able to kill the mouse, but not without sustaining heavy injuries'")
          #          time.sleep(para.Mwait)
                    print("'Interested in seeing what could happen at even higher exposure levels, I repeated my experiment with 3 new mice, increasing the exposure to 10x the levels of before.'")
           #         time.sleep(para.Mwait)
                    print("'Immediately, the mice appeared to fall under extreme pain, though I decided to once again wait the full 24 hours to see what the effects would be'")
            #        time.sleep(para.Mwait)
                    print("'When I returned, I was met with a gruesome sight. One of the mice had murdered the other two, following my expectations. What I hadn't expected however, was that the zathene energy had forcibly mutated the mouse, causing several changes to occur on its body'")
             #       time.sleep(para.Mwait)
                    print("''These changes were but not limited to:''")
              #      time.sleep(para.Mwait)
                    print(" '- Increased size'")
               #     time.sleep(para.Swait)
                    print(" '- The growth of additional rows of sharp teeth'")
                #    time.sleep(para.Swait)
                    print(" '- Sharpened claws'")
                 #   time.sleep(para.Swait)
                    print(" '- Yellow discolouration of the eyes'")
                  #  time.sleep(para.Swait)
                    print(" '- Growth of additional eyes on its back and forehead'")
                   # time.sleep(para.Swait)
                    print("'- Malformed snout'")
#                    time.sleep(para.Swait)
                    print("'- Overproduction and build up of bodily fluids'")
 #                   time.sleep(para.Swait)
                    print("'- Large swelling and tumour growth all over the body'")
  #                  time.sleep(para.Mwait)
                    print("\n'The mouse also displayed even higher levels of aggression than before, even trying to attack me through the glass window in its enclosure'")
   #                 time.sleep(para.Mwait)
                    print("'Thankfully, as the glass was bulletproof, it was not able to succeed, and I was able to euthanise the creature by flooding its cage with carbon monoxide'")
    #                time.sleep(para.Mwait)
                    print("\n'In conclusion, while seemingly harmless in small doses, prolonged exposure to large doses of zathene energy appear to cause extreme amounts of aggression in the individual, and even mutating them if the dosage is high enough'")
     #               time.sleep(para.Mwait)
                    print("'However, as the experiment was only conducted on mice, it is currently unknown if the same results could apply to larger animals such as humans'")
      #              time.sleep(para.Mwait)
                    print("'Overall, I would suggest to exercise caution around the implementation of zathene energy, and will be reporting my findings to the head of Vexon Industries'")

                elif contents == "d":
                    print("Research papers are boring")
                    break

class stalkerc(encounters):
    def __init__(self):
        super().__init__(20, 101, "stalker")
    def text(self):
        stalking.switch = True
        print("You've caught someone's attention")

# class beelzebubc(encounters):
#     def __init__(self):
#         super().__init__(15, 50, "beelzebub")
#     def text(self):
#         print("Combat encounter: glutton")

class blackcatc(encounters):
    def __init__(self):
        super().__init__(15, 101, "blackcat")
    def text(self):
        #print("eat cat to lose sanity for hunger or pet cat for luck decrease")
        #print("If sanity is low and pet cat, fight cheshire")
        print("You find a small black cat in the middle of the street")
        time.sleep(para.Mwait)
        print("It looks at you and lets out a small meow")
        time.sleep(para.Mwait)
        pet = input("A: Pet the cat\nB: Consume the cat\n").lower()
        if pet == "a":
            print("As you approach the cat, it bends down for you to pet it")
            time.sleep(para.Mwait)
            print("You trace your fingers along the cat's silky fur, and it lets out a satisfied purr in response")
            time.sleep(para.Mwait)
            print("The act puts you at ease")
            time.sleep(para.Swait)
            print("[Sanity +"+str(para.smallrestore)+"]")
            player.sanity += para.smallrestore
            time.sleep(para.Mwait)
            print("Wait, wasn't there an old saying about black cats?")
            time.sleep(para.Mwait)
            print("I'm sure it wasn't important")
            time.sleep(para.Mwait)
            print("[Luck -1]")
            player.luck -= 1

        elif pet == "b":
            print("As you approach the cat, it bends down for you to pet it")
            time.sleep(para.Mwait)
            print("But instead of petting it, your hands roughly grab the cat to bring it towards your mouth")
            time.sleep(para.Mwait)
            print("The feline shrieks and claws in order to escape your grip, but to no avail")
            time.sleep(para.Mwait)
            print("The poor kitten meets its demise as your teeth bite down on its throat")
            time.sleep(para.Mwait)
            print("You are wracked with guilt for killing such an innocent soul, yet your hunger is greater still")
            time.sleep(para.Mwait)
            print("[Hunger +" + str(para.smallrestore) + "]")
            player.hunger += para.smallrestore
            player.sanity -= para.smallchange
            print("[Sanity -" + str(para.smallchange) + "]")

class restc(encounters):
    def __init__(self):
        super().__init__(17, 101, "rest")
    def goodsleep(self):
        print("You instantly fall asleep, ridding yourself of all the exhaustion acquired on your adventure")
        time.sleep(para.Mwait)
        print("When you wake up, you feel reinvigorated and ready to take on the world")
        time.sleep(para.Mwait)
        player.maxhealth += 1
        player.health = player.maxhealth
        player.hunger -= para.smallchange
        player.sanity += para.smallrestore
        print("[Max Health +1]")
        print("[Health fully restored]")
        print("[Sanity +"+str(para.smallrestore)+"]")
        print("[Hunger -"+str(para.smallchange)+"]")

    def badsleep(self):
        print("You find yourself tossing and turning throughout the night, unable to stay asleep")
        time.sleep(para.Mwait)
        print("Still, any amount of rest is better than nothing")
        time.sleep(para.Mwait)
        y = player.health
        player.health += (player.maxhealth/2)
        player.hunger -= para.smallchange
        print("[Health +"+str(player.maxhealth/2)+"]")
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
        fight(batter)
        print("The second masked man attacks!")
        time.sleep(para.Mwait)
        fight(batter)

    def robbed(self):
        print("You sleep soundly through the night")
        time.sleep(para.Mwait)
        z = player.sanity
        player.health = player.maxhealth
        player.hunger -= para.smallchange
        print("[Health fully restored]")
        print("[Sanity +" + str(para.smallrestore)+"]")
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
        player.hunger -= para.smallchange
        player.sanity -= 30
        print("[Health +" + str(player.maxhealth/2) + "]")
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
        super().__init__(20, 101, "mugging")
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
            if not hasitems:
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
                if random.randint(1, 100) + player.luck + player.atk < 55:
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
            fight(batter)
            print("The second masked man attacks!")
            fight(batter)
            print("'Oh no ya don't!'")
            time.sleep(para.Swait)
            print("The third masked man attacks!")
            fight(batter)

        if betray == True:
            print("You pass on through, now with considerably lighter pockets than before")

# class mansionc(encounters):
#     def __init__(self):
#         super().__init__(15, 101, "mansion")
#     def text(self):
#         print("Stay at creepy guy's mansion")

class doctorc(encounters):
    def __init__(self):
        super().__init__(13, 101, "doctor")
    def text(self):
        print("You encounter a man in a bloodstained doctor's uniform")
        time.sleep(para.Mwait)
        print("He shambles towards you, pulling down his mask to reveal a crooked row of yellow teeth fixed in a menacing grin")
        time.sleep(para.Mwait)
        print("'Ah, a healthy donor! It's been so long since I've had someone like you.'")
        time.sleep(para.Mwait)
        print("'Please, won't you consider donating your blood for those in need? There are many dying patients who could use it much more than you, and I'll offer a reward too!'")
        time.sleep(para.Mwait)
        print("The doctor raises a long rusted needle, covered in bits of dried blood")
        time.sleep(para.Mwait)
        print('Accept the "doctor'+"'"+'s", request?')
        #Should read as "Accept the "doctor's" request?
        time.sleep(para.Swait)
        print("A: Yes")
        print("B: No way!")
        x = input()
        x = x.lower()
        if x == "a":
            print("The doctor roughly jabs the needle into your arm with no concern for your pain")
            time.sleep(para.Mwait)
            print("Blood spurts out of your arm with vigor, as the doctor flails around trying to collect it all in a bottle")
            time.sleep(para.Mwait)
            print("The sight and amount of  blood leaving your body makes you dizzy, and you find yourself losing consciousness")
            time.sleep(para.Mwait)
            print("[Health -" + str(para.largeschange) + "]")
            player.health -= para.largeschange
            time.sleep(para.Mwait)
            print("When you come to, the doctor stands before you, an empty bottle clutched in his hands")
            time.sleep(para.Mwait)
            print("'Unfortunately we were not able to collect much blood this time round, but a deal is a deal so I shall give you your compensation'")
            time.sleep(para.Mwait)
            print("[Gold +2]")
            player.gold +=2
            time.sleep(para.Mwait)
            print("It could just be your imagination, but you swear the doctor seems much younger than before")
            time.sleep(para.Mwait)
            print("'I sincerely hope you come again, many patients are counting on your blood, and I- we simply MUST have it!'")

        else:
            print("You turn to leave, you already have yourself to worry about")
            time.sleep(para.Mwait)
            print("Suddenly, your arm is grasped by the doctor's!")
            time.sleep(para.Mwait)
            print("'Oh I don't think so. Your blood is simply to precious for us to give up!'")
            time.sleep(para.Mwait)
            print("You pull and pull, but the doctor's grip on you remains firm")
            time.sleep(para.Mwait)
            if random.randint(0, 100) + player.luck + player.atk > 60:
                print("Eventually, a well placed kick causes him to let go, and you seize the opportunity to escape")
            else:
                if fight(doctor):
                    x = input("The remains of the doctor lie before you\nA: Consume\nB: Loot\nC: Leave\n").lower()
                    if x == "c":
                        print("You aren't getting nearer to that psycho")
                    else:
                        if random.randint(1,100)+player.luck < 10:
                            print("As you bend down, you hand is grasped by the doctor!")
                            time.sleep(para.Mwait)
                            print("'I don't think so. I'm not done with you yet!'")
                            fight(doctor)

                        elif x == "a":
                            print("You consume the doctor")
                            time.sleep(para.Mwait)
                            print("He's all juice and no meat")
                            time.sleep(para.Swait)
                            print("[Hunger +" + str(para.smallrestore) + "]")
                            print("[Sanity -" + str(para.largechange) + "]")
                            player.hunger += para.smallrestore
                            player.sanity -= para.largechange

                        elif x == "b":
                            print("You loot the doctor's corpse")
                            from invmenu import words
                            time.sleep(para.Mwait)
                            new = random.randint(0, len(words)-1)
                            print("You found some", words[new])
                            player.inv[words[new]] += 1


class sacrificec(encounters):
    def __init__(self):
        super().__init__(7, 101, "sacrifice")
    def text(self):
        #print("Sacrifice health for statboost/lower doom")
        def dud():
            print("But nothing happens")

        def health():
            print("You are blessed with improved vitality!")
            print("[Max Health +1]")
            player.maxhealth += 1

        def luck():
            print("You are blessed with good fortune!")
            print("[Luck +5]")
            player.luck += 5

        def strength():
            print("You feel blessed with great strength!")
            print("[Attack +1]")
            player.atk += 1

        def gold():
            print("You look down at your feet, and find yourself blessed with great riches!")
            print("[Gold +5]")
            player.gold += 5

        def heal():
            print("You are blessed with good health!")
            print("[Health fully restored]")
            player.health = player.maxhealth

        def sane():
            print("You are blessed with a clear mind!")
            print("[Sanity fully restored]")
            player.sanity = 100

        def full():
            print("You are blessed with fulfillment!")
            print("[Hunger fully restored]")
            player.hunger = 100

        def bad():
            print("It feels good")
            print("[Sanity -"+str(para.smallchange)+"]")


        print("You find an altar with a large spike protruding from it")
        time.sleep(para.Mwait)
        print("You feel the sharp edge of the spike calling out to you")
        time.sleep(para.Mwait)
        print("The gods must be appeased")
        time.sleep(para.Mwait)
        x = input("A: Sacrifice health\nB: Leave\n").lower()
        if x == "b":
            print("It takes all of your mental energy to pull yourself away from the shrine")
            time.sleep(para.Mwait)
            print("[Sanity -"+str(para.smallchange)+"]")
            player.sanity -= para.smallchange
        else:
            while True:
                print("You pierce your hand on the altar, watching as the blood trickles down to the base")
                time.sleep(para.Swait)
                print("[Health -1]")
                player.health -=1
                time.sleep(para.Lwait)
                blessings = [dud, health, luck, strength, gold, bad]
                if player.maxhealth/2 >= player.health:
                    blessings.append(heal)
                if 50 >= player.sanity:
                    blessings.append(sane)
                if 50 >= player.hunger:
                    blessings.append(full)
                blessings[random.randint(0, len(blessings) - 1)]()
                x = input("A: Sacrifice more\nB: Stop\n").lower()
                if x == "b":
                    break

class witchc(encounters):
    def __init__(self):
        super().__init__(15, 101, "witch")
    def text(self):
        #print("Offered a potion which will restore/harm or raise/lower a stat")
        print("You find a rusty shack, tucked away in the alleyways")
        time.sleep(para.Mwait)
        print("Upon entering, you find an old hag hunched over a cauldron, cackling wildly")
        time.sleep(para.Mwait)
        print("Her face is so covered in warts, that it's impossible to tell if she's even still human or not")
        time.sleep(para.Mwait)
        print("Upon spotting you, she grabs a mug and scoops something out of the cauldron, crawling over to you")
        leave = False
        time.sleep(para.Mwait)
        print("'DRINK!'")
        time.sleep(para.Mwait)
        x = input("A: Drink\nB: don't drink\n").lower()
        if x == "b":
            print("The woman seems quite agitated")
            time.sleep(para.Mwait)
            print("'DRINK!'")
            time.sleep(para.Mwait)
            x = input("A: Drink\nB: don't drink\n").lower()
            if x == "b":
                leave = True

        if leave == False:
            print("The strange liquid bubbles and froths in the mug")
            time.sleep(para.Mwait)
            print("Closing your eyes, you quickly gulp it down")

            def dud():
                print("The potion is fairly tasteless, and you notice no odd effects")

            def health():
                print("The potion is thick and hot, with an earthy taste to it")
                time.sleep(para.Lwait)
                print("[Max Health +1]")
                player.maxhealth += 1

            def luck():
                print("The potion has a tangy, sparkling taste, almost hurting your tongue")
                time.sleep(para.Lwait)
                print("[Luck +3]")
                player.luck += 3

            def strength():
                print("The potion is overwhelmingly strong, and it takes you all of your effort to resist throwing it back up")
                time.sleep(para.Lwait)
                print("[Attack +1]")
                player.atk += 1

            def lhealth():
                print("The potion is sickly sweet, sticking to your throat in large globs")
                time.sleep(para.Lwait)
                print("[Max Health -1]")
                player.maxhealth -= 1

            def lluck():
                print("The potion is a bitter remedy of herbs and animal hair, which gets caught in your throat")
                time.sleep(para.Lwait)
                print("[Luck -3]")
                player.luck -= 3

            def lstrength():
                print("The potion is extremely salty, and you are filled with nausea")
                time.sleep(para.Lwait)
                print("[Attack -1]")
                player.atk -= 1

            def heal():
                print("The potion is a flavourful broth which warms your whole body")
                time.sleep(para.Lwait)
                print("[Health fully restored]")
                player.health = player.maxhealth

            def sane():
                print("The potion is cold and refreshing, with a crisp blue flavour")
                time.sleep(para.Lwait)
                print("[Sanity +"+str(para.smallchange)+"]")
                player.sanity += para.smallchange

            def full():
                print("The potion turns out to be a delicious stew")
                time.sleep(para.Lwait)
                print("[Hunger +" + str(para.smallchange) + "]")
                player.hunger += para.smallchange

            def lheal():
                print("The potion is extremely hot, burning your mouth as you drink it")
                time.sleep(para.Lwait)
                print("[Health -"+str(para.smallschange)+"]")
                player.health -= para.smallschange

            def lsane():
                print("The potion is completely and utterly revolting, you never thought a taste so bad could possibly exist")
                time.sleep(para.Lwait)
                print("[Sanity -" + str(para.smallchange) + "]")
                player.sanity -= para.smallchange

            def lfull():
                print("The potion has a dull, slightly bitter taste, and makes you feel empty inside as you consume it.")
                time.sleep(para.Lwait)
                print("[Hunger -"+str(para.smallchange)+"]")


            flavours = [dud, health, luck, strength, lhealth, lluck, lstrength, heal, sane, full, lheal, lsane, lfull]
            flavours[random.randint(0, len(flavours) - 1)]()

# class cultc(encounters):
#     def __init__(self):
#         super().__init__(17, 101, "cult")
#     def text(self):
#         print("Perform ritual with cult to raise doom or fight members consecutively")
#         print("If doom is high, cultists get a stat increase")
#
# class crawlerc(encounters):
#     def __init__(self):
#         super().__init__(17, 101, "crawler")
#     def text(self):
#         print("Combat encounter: crawler")

class mirrorc(encounters):
    def __init__(self):
        super().__init__(2, 101, "mirror")
    def text(self):
        print("You look in the mirror")
        time.sleep(para.Mwait)
        if player.sanity <= 50:
            print("Your reflection lunges at you!")
            fight(mimic)
        elif player.luck+random.randint(0,100) > 30 == True:
            print("It's you")
        else:
            print("That's not you")
            time.sleep(para.Swait)
            print("[Sanity -" + str(para.smallchange) + "]")
            player.sanity -= para.smallchange

class hunterc(encounters):
    def __init__(self):
        super().__init__(15, 101, "hunter")
    def text(self):
        print("A deafening bang echoes down the alleyway, ringing in your ears")
        time.sleep(para.Mwait)
        print("You turn around and see what seems to be a man wearing a deer head reloading his rifle, spewing smoke into the surroundings.")
        time.sleep(para.Lwait)
        print("He finishes reloading and once again points his gun at his target, which you realise with horror- is you.")
        time.sleep(para.Mwait)
        x = input("A: Fight\nB: Run away\nC: Zig-zag away\nD: find cover\nE: Dodge roll\n").lower()
        brawl = False
        if x == "a":
            print("You charge towards the deerman, but he fires his rifle before you can reach him!")
            time.sleep(para.Mwait)
            print("Your attempted assault has left you wide open to be hit, and the bullet lands a clear hit on your shoulder")
            time.sleep(para.Mwait)
            print("An explosion of gore erupts from your shoulder, as you are driven back in shock")
            print("[Health -"+str(hunter.atk)+"]")
            player.health -= hunter.atk
            time.sleep(para.Mwait)
            print("However, you don't have time to worry about your shoulder, as the figure has started reloading his gun")
            print("Seizing the opportunity, you run in to attack!")
            brawl = True

        elif x == "b":
            print("You attempt to run away from the man")
            time.sleep(para.Mwait)
            print("However, by fleeing away you give the hunter a clean shot at you!")
            time.sleep(para.Mwait)
            print("Another deafening boom rings out, followed by a searing pain in your legs as you fall to the ground")
            time.sleep(para.Swait)
            print("[Health -" + str(hunter.atk) + "]")
            player.health -= hunter.atk
            time.sleep(para.Mwait)
            print("The smoke emitted from the gun obscures your vision, but you can hear footsteps approaching you from behind")
            time.sleep(para.Mwait)
            y = input("A: Keep fleeing\nB: Hide\n").lower()
            if y == "a":
                print("Unable to move your legs, you frantically pull yourself along the ground, terror filling your mind")
                time.sleep(para.Mwait)
                if player.health <= hunter.atk:
                    print("However, your heart drops when you feel a long metal object poke the back of your head")
                    time.sleep(para.Mwait)
                    print("The sound of the explosion ruptures your eardrums, but you are unable to think about that for now")
                    time.sleep(para.Mwait)
                    print("In fact, you are unable to think about anything at all.")
                    time.sleep(para.Mwait)
                    print("The last thing you feel is an agonising pain in your head, before it bursts into a million pieces")
                    time.sleep(para.Mwait)
                    print("[GAME OVER]")
                    player.health -= hunter.atk
                else:
                    print("However, your progress is halted as another shot rings out, mutilating your arm")
                    time.sleep(para.Mwait)
                    print("Unable to retreat any further, you are forced to face the threat before you")
                    brawl = True

            elif y == "b":
                print("Taking advantage of the smoke in the air, you frantically scan the area looking for a place to hide")
                time.sleep(para.Mwait)
                print("Luckily, you spot a pile of corpses, and you are barely able to pull yourself into them before the deerman arrives")
                time.sleep(para.Mwait)
                print("The man stands there, seemingly searching for you as you remain covered in the bodies")
                time.sleep(para.Mwait)
                print("The foul stench of rotting corpses is unbearable, and you notice they are all riddled with bulletholes.")
                time.sleep(para.Swait)
                print("[Sanity -"+str(para.smallchange)+"]")
                player.sanity -= para.smallchange
                print("Right when it seems like he's about to leave, he turns around and fires a final shot into the pile of corpses")
                time.sleep(para.Mwait)
                print("The shockwave of the bullet reverberates through you, but you are luckily unharmed")
                time.sleep(para.Mwait)
                print("Not long after, he leaves")
                print("And so do you")

        elif x == "c":
            print("You attempt to run away from the creature, taking a zig-zag pattern to avoid being shot")
            time.sleep(para.Mwait)
            print("Seeing your escape, the monster releases another shot at you")
            time.sleep(para.Mwait)
            if random.randint(1, 100) + player.luck >= 25:
                print("However, the bullet shoots past you, and you manage to make your escape")
                time.sleep(para.Mwait)
            else:
                print("Despite your best efforts to evade it, the bullet pierces through your shoulder, sending pain shooting through your body")
                time.sleep(para.Mwait)
                print("In spite of the pain, you grit your teeth and push on, making your escape before the man can reload his gun again.")
                time.sleep(para.Mwait)
                print("[Health -" + str(hunter.atk) + "]")
                player.health -= hunter.atk
            print("[Hunger -"+str(para.smallchange)+"]")
            player.hunger -= para.smallchange

        elif x == "d":
            print("Desperate to not be in the bullets path, you duck behind a fence as the gunshot rings out")
            time.sleep(para.Mwait)
            print("The force of the shot causes the fence to splinter into a million pieces, however you are unharmed")
            time.sleep(para.Mwait)
            print("Before the man can reload again, you quickly dash around a corner, pressing your back against the wall")
            time.sleep(para.Mwait)
            print("You hear boots clapping against the pavement as the hunter approaches your hiding position")
            time.sleep(para.Mwait)
            corner = input("A: Attack\nB: Escape\n").lower()
            if corner == "a":
                print("Readying yourself, you ambush the creature as soon as it turns the corner!")
                brawl = True

            elif corner == "b":
                print("You manage to escape before the monster can find you again")

        elif x == "e":
            print("You throw yourself forwards, hoping to dodge-roll out of the way of the creature's attack")
            time.sleep(para.Mwait)
            print("Unfortunately, you soon find that dodge-rolls are a lot harder to perform in real life than in a game, as you land on the ground with a thud")
            time.sleep(para.Mwait)
            print("However, your attempt was still able to get you clear of the bullet's path!")
            time.sleep(para.Mwait)
            print("Drawing your dagger, you attack the hunter before it can reload it's gun again!")
            brawl = True






        if brawl == True:
            if fight(hunter):
                x = input("The body of the hunter lies before you\nA: Consume\nB: Loot for items\nC: Steal gun\nD: leave\n").lower()
                if x == "a":
                    print("You draw your dagger and begin to carve out chunks of flesh to consume")
                    time.sleep(para.Mwait)
                    print("It's a fitting end for such a creature")
                    time.sleep(para.Mwait)
                    print("Though the knowledge that it may have once been human still haunts you")
                    print("[Hunger +"+str(para.largerestore)+"]")
                    player.hunger += para.largerestore
                    print("[Sanity -"+str(para.largechange)+"]")
                    player.sanity -= para.largechange

                elif x == "b":
                    print("You loot the corpse for items")
                    new = random.randint(0, len(words)-1)
                    print("You found some", words[new])
                    player.inv[words[new]] += 1

                elif x == "c":
                    print("You took the hunter's rifle")
                    player.gun = True
                    player.inv["bullets"] = 3
                    words.append("bullets")


class mimicc(encounters):
    def __init__(self):
        super().__init__(25, 50, "mimic")
    def text(self):
        print("You see someone standing in the distance")
        time.sleep(para.Mwait)
        print("Wait, is that... You?")
        fight(mimic)

class lore3c(encounters):
    def __init__(self):
        super().__init__(20, 101, "lore3")
    def text(self):
        #print("cult room")
        print("You find a broken laptop lying on the ground")
        time.sleep(para.Mwait)
        print("The screen seems to be frozen, unable to display anything other than a single open email")
        time.sleep(para.Mwait)
        snoop = input("Read the email?\nA: Yes\nB: No\n").lower()
        if snoop == "a":
            print("\n\n\n\nTo: vanessa.corpra@vexonindustries.com\nSubject: Disruptive behaviour in the workplace\n\nHi V,\n\nSo I've recently been observing some really weird behaviour from some of my other co-workers in D14, which I would not only call off-putting, but outright disruptive.\nAnd I've been told that I'm supposed to tell you about it, since you're the new HR manager, which is why I'm emailing you.\nBasically, ever since the higherups starting using that 'zathene energy' stuff, they've been acting really weird.\nThey keep on speaking super strangely, they're never around as much as before, and they keep on sending out super weird directives for us to follow.\nLike one time they ordered we make some changes to our deep-sea diving robots, such as adding reinforced armour, a smorgesborg of concealed weapons and quote 'Claws containing 10 inch blades capable of disembowling and deboning targets in under 3 milliseconds'.\nNow, please tell me WHY THE HELL a deep-sea diving robot would need 30 different types of guns and '10 inch blades'?\nWhat the f*ck is in the ocean, the goddamn Kracken?\nWell apparently not, since we were specifically told to ensure 'maximum effectiveness against humanoid targets'.\nWhat's more, some of these seem counter-intuitive, such as removing the webbed-feet and rotors in favour of improved mobility on land.\nI don't know what the hell they plan to do with these things, but something tells me it's not just oil drilling anymore.\n\nI'll never forget the last time I saw one of the Directors in person.\nIt was nearly midnight, and I had just received an order to bring a pound of steak into his office.\nBy now, I had gotten used to receiving bizarre requests like this, so I complied.\nBut when I got to his office, he seemed... off.\nThe entire room was pitch black, courtesy of every single light source being sealed off.\nIn the middle of the room sat the Director, perfectly still, not even blinking.\nI tried to call out to him, but he simply just sat there and stared at me, repeating some foreign phrase over and over.\n\nNow while this is disturbing, and no doubt a waste of company resources, that's not what made me write this email.\nYou see, I'm afraid whatever caused the Directors to act so weird has started to influence my other co-workers too.\nRecently I've noticed my co-workers becoming a lot quieter, and less responsive, as if they're in a trance.\nThey've also been speaking that same creepy language the Director I saw was speaking too.\nNow don't get me wrong, I'm not racist. I respect other people's languages and cultures as much as the next guy, but this language they speak, there's just something evil about it, yknow?\nYou'd know what I meant if you heard it, the sounds they make are so disturbing and unnatural, and every time I hear it I get shivers down my spine.\nWe've also been having frequent 'work meetings', except all everyone does is gather in a circle round the room and chant things!\nThe whole thing feels like a god-damn cult instead of a company.\nThe final straw, was when everyone started turning up to work wearing these robes.\nThey claimed it was simply 'corporate mandated dress code', well I call bullsh*t!\nOnly the CEO, Maxim Vexon has the authority to change the dress code and if he did, it would have been in the monthly announcements!\nWhen I told a co-worker this, he simply shook his head at me and said 'Not Maxim, even higher. More senior.'\nThis is absolute blasphemy!\nAt Vexon Industries, NOBODY holds more authority than the CEO, the mere SUGGESTION that someone could claim otherwise makes it clear to me that this department has completely lost its rocks!\n\nBecause of this, I sincerely believe that leaving this department as is would be a detriment to the company.\nClearly, everyone has lost their values and are no longer working within the company's interests, so I suggest the best course of action be to let them all go and hope the next hires don't turn out to be lunatics like their predecessors.\nPlease do something about this quickly, these people seem to be getting crazier by the minute, and I don't like the looks some of them are starting to give me.\n\n\n\nSincerely, Owen from the engineering department")
        else:
            print("It's not nice to snoop on other people's conversations")

# class trapc(encounters):
#     def __init__(self):
#         super().__init__(25, 101, "trap")
#     def text(self):
#         print("Chance for item or take damage")
#
# class fleshortcutc(encounters):
#     def __init__(self):
#         super().__init__(25, 101, "fleshortcut")
#     def text(self):
#         print("fleshortcut")
#
# class amigarac(encounters):
#     def __init__(self):
#         super().__init__(30, 101, "amigara")
#     def text(self):
#         print("go through crack, gain distance but lose health, max sanity and hunger to 50 and gain attack")

class holesc(encounters):
    def __init__(self):
        super().__init__(20, 101, "holes")
    def text(self):
        #print("Sees holes on hand, can either cut it out and take damage, or let holes spread for reduced max hp")
        print("Your left hand has been feeling sore for a while now")
        time.sleep(para.Mwait)
        print("Upon looking down, you find a large cluster of blisters in a spiral pattern growing on the back of your palm!")
        time.sleep(para.Mwait)
        x = input("A: Cut it out\nB: Ignore\n").lower()
        if x == "a":
            print("You aren't going to take any chances")
            time.sleep(para.Mwait)
            print("Grasping the hilt of your dagger, you sink the blade into your skin, attempting to carve out the spiral")
            time.sleep(para.Mwait)
            print("Your hand flares with pain as the steel blade saws its way around the pattern")
            time.sleep(para.Mwait)
            print("After what feels like an eternity of agony, you successfully separate it from your hand")
            print("The bright mass of discarded flesh falls to the ground with a splat")
            time.sleep(para.Mwait)
            print("[Health -"+str(para.smallschange)+"]")
            player.health -= para.smallschange

        else:
            print("You decide to ignore the unnatural pattern on your hand")
            time.sleep(para.Mwait)
            print("It's probably nothing too serious... right?")
            time.sleep(para.Mwait)
            print("However this turns out to be false, as you soon find the blisters spreading across your arm and covering your entire torso")
            time.sleep(para.Mwait)
            print("The pain is unbearable, you feel like they are draining you of your life force")
            time.sleep(para.Mwait)
            print("[Max Health -1]")
            player.maxhealth -= 1

class saviorc(encounters):
    def __init__(self):
        super().__init__(22, 101, "savior")
    def text(self):
        #print("Fight consecutive battles and be rewarded or ignore at sanity cost")
        print("You hear a scream ringing out from further ahead")
        time.sleep(para.Mwait)
        print("Rushing towards it, you find another survivor being attacked by a gang of monsters!")
        time.sleep(para.Mwait)
        print("Intervene and save the civilian?")
        time.sleep(para.Swait)
        save = input("A: Yes\nB: It's too risky\n").lower()
        if save == "a":
            enemies = ["creeps", "gang", "mutants", "skinwalker", "blindM"]
            monster = enemies[random.randint(0, 3)]
            win = False
            if monster == "creeps":
                if fight(doctor):
                    print("The second assailant attacks you!")
                    if fight(stalker):
                        win = True

                    print("Th")
            elif monster == "gang":
                if fight(batter):
                    print("The second masked man approaches!")
                    if fight(batter):
                        print("The third masked man approaches!")
                        if fight(batter):
                            print("You attack the final masked man!")
                            if fight(batter):
                                win = True

            elif monster == "mutants":
                if fight(gnasher):
                    print("A second monster approaches!")
                    if fight(gnasher):
                        print("You attack the final monster!")
                        if fight(zombie):
                            win = True

            elif monster == "blindM":
                if fight(gnasher):
                    print("A second monster charges at you!")
                    if fight(gnasher):
                        print("The final monster makes his appearance!")
                        if fight(digger):
                            win = True

            elif monster == "skinwalker":
                if fight(skinwalker):
                    win = True

            if win == True:
                print("The survivor turns to you")
                time.sleep(para.Mwait)
                print("'Thank you so much!'")
                print("'Here, take some of my supplies. I know it's not much, but I hope this can repay you'")
                time.sleep(para.Mwait)
                print("[Gold +2]")
                print("[Meat +1]")
                print("[Pills +1]")
                print("[Bandages +1]")
                player.gold += 2
                player.inv["meat"] += 1
                player.inv["pills"] += 1
                player.inv["bandages"] += 1
                time.sleep(para.Lwait)
                print("However, the survivor's face grows pale as they look upon your face")
                time.sleep(para.Mwait)
                print("'Wait, you're not... Oh god'")
                time.sleep(para.Mwait)
                print("With a terrified expression on their face, the survivor flees!")

        else:
            print("You run away, trying your best to ignore the screams which ring out from behind you")
            print("[Sanity -"+str(para.largechange)+"]")
            player.sanity -= para.largechange

# class amalgamc(encounters):
#     def __init__(self):
#         super().__init__(35, 101, "amalgam")
#     def text(self):
#         print("Combat encounter: Amalgam")

# class angelc(encounters):
#     def __init__(self):
#         super().__init__(35, 50, "angel")
#     def text(self):
#         print("Combat encounter: Angel")

class gods_callingc(encounters):
    def __init__(self):
        super().__init__(15, 50, "gods_calling")
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
        else:
            print("You shakily draw a knife and plunge it into your chest")
            time.sleep(para.Mwait)
            print("[Health -" + str(player.atk) + "]")
            player.health -= player.atk

# class maskedbasec(encounters):
#     def __init__(self):
#         super().__init__(40, 101, "masked base")
#     def text(self):
#         print("Can either sneak by, steal food or turn back")
#         print("stealing food has higher chance of failure, turning back results in loss of distance")
#         print("if caught, fight 2 masked men and then leader")
#
# class terrorc(encounters):
#     def __init__(self):
#         super().__init__(40, 50, "terror")
#     def text(self):
#         print("Combat encounter: Terror")
#
# class dollc(encounters):
#     def __init__(self):
#         super().__init__(40, 101, "doll")
#     def text(self):
#         print("Combat encounter: doll")

# class hydrac(encounters):
#     def __init__(self):
#         super().__init__(40, 101, "hydra")
#     def text(self):
#         print("Combat encounter: Hydra")

class skinwalkerc(encounters):
    def __init__(self):
        super().__init__(30, 101, "skinwalker")
    def text(self):
        fight(skinwalker)

# class HADc(encounters):
#     def __init__(self):
#         super().__init__(40, 101, "H.A.D")
#     def text(self):
#         print("Combat encounter: H.A.D")




def stalk5():
    print("You feel like someone is right behind you")
    time.sleep(para.Mwait)
    x = input("Turn around?\nA: Yes\nB: No\n").lower()
    if x == "a":
        print("You turn around")
        time.sleep(para.Mwait)
        if random.randint(1, 100) + player.luck < 50:
            print("But there was no-one there")
            stalking.switch = False
            stalking.counter = 3
        else:
            print("You see a all man clutching a knife in his hands grinning back at you")
            if fight(stalker):
                x = input("The corpse of the stalker lies in front of you\nA: Consume\nB: Leave\n").lower()
                if x == "a":
                    print("Unfortunately, there is not much meat on his bones, but you take what you can get")
                    time.sleep(para.Mwait)
                    x = player.hunger
                    player.hunger += para.smallrestore
                    print("[Hunger +" + str(player.hunger - x) + "]")
                    player.sanity -= para.largechange
                    print("[Sanity -" + str(para.largechange) + "]")

        stalking.counter = 0
        stalking.switch = False
    else:
        print("You're probably just imagining it, right?")
        time.sleep(para.Swait)
        stalking.counter = 3


flavour = flavourc()
Nsaneflavour = Nsaneflavourc()
eldritchvisions = eldritchvisionsc()
# foodfind = foodfindc()
# pillfind = pillfindc()
# bandagefind = bandagefindc()
essentials = essentialsc()
goldfind = goldfindc()
itemfind = itemfindc()
stargaze = stargazec()
eslime = slimec()
ezombie = zombiec()
eshadow = shadowc()
lootcorpse = lootcorpsec()
lore1 = lore1c()
shrine = shrinec()
konami = konamic()
drink = drinkc()
deersac = deersacc()
ebatter = batterc()
shop = shopc()
egnasher = gnasherc()
esorrow = sorrowc()
butchershop = butchershopc()
eraven = ravenc()
tunnelchase = tunnelchasec()
lore2 = lore2c()
estalker = stalkerc()
blackcat = blackcatc()
rest = restc()
mugging = muggingc()
#mansion = mansionc()
edoctor = doctorc()
sacrifice = sacrificec()
witch = witchc()
#cult = cultc()
#altar = altarc()
#ecrawler = crawlerc()
mirror = mirrorc()
ehunter = hunterc()
emimic = mimicc()
lore3 = lore3c()
#trap = trapc()
#fleshortcut = fleshortcutc()
#amigara = amigarac()
holes = holesc()
savior = saviorc()
#emalgam = amalgamc()
#angel = angelc()
gods_calling = gods_callingc()
# maskedbase = maskedbasec()
# eterror = terrorc()
# edoll = dollc()
#hydra = hydrac()
eskinwalker = skinwalkerc()
#HAD = HADc()

#encounters = different events which can occur
eventable = [flavour, Nsaneflavour, eldritchvisions, essentials, goldfind, itemfind, stargaze, eslime, ezombie, eshadow, lootcorpse, lore1, shrine, konami, deersac, drink, ebatter, egnasher, esorrow, butchershop, tunnelchase, shop, lore2, eraven, estalker,  blackcat, rest, mugging, edoctor, sacrifice, mirror, ehunter, emimic, witch, lore3, gods_calling, holes, savior, eskinwalker]
last = ""

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