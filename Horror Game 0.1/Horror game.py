import random
import time
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
#Player stats used to be stored as a list and as I only recently changed it to a class, most code still calls for list values.
#List values so the rest of the code makes sense:
#maxhealth = 0
#health = 1
#hunger = 2
#sanity = 3
#atk = 4
#luck = 5
#xp = 6
# gold = 7
#Accuracy and doom weren't added yet.





#Function used when an event has a random outcome
def skillcheck(luck, minnumber):
#minnumber is the percentage chance of success. 75% = (minnumber = 75)
    if (random.randint(1, 100) + luck) >= 100-minnumber:
        return True
    else:
        return False

#Determines whether to add ammo to the itempool
hasgun = False
stalking = -1
distance = 0
#Items get appended to the list when added to inventory, duplicates increase the value of the corresponding variable
items = ["meat"]
food = 5
bandage = 0
pills = 0
knives = 0
acid = 0
rbtfoot = 0
roids = 0
ammo = 0
charm = 0
 

#Data values each encounter holds
class encounters:
    def __init__(self, diff, san, name, fight):
        self.diff = diff
        self.san = san
        self.fight = fight
        self.name = name
        #diff = difficulty (number of steps until event can be included)
        #san = sanity (Maximum sanity value event can occur at)
        #fight = Whether event is a combat encounter or not (will be used when an event outcome leads to random fight)
        #name = name of encounter

#Encounters:
flavour = encounters(0, 101, "flavour", False)
Nsaneflavour = encounters(1, 50, "Nsaneflavour", False)
itemfind = encounters(1, 101, "itemfind", False)
slime = encounters(2, 101, "slime", True)
zombie = encounters(2, 101,"zombie", True)
shadow = encounters(2, 50, "shadow", True)
lore1 = encounters(3, 100, "lore1", False)
shrine = encounters(3, 101, "shrine", False)
amigara = encounters(3, 101, "amigara", False)
drink = encounters(5, 101, "drink", False)
batter = encounters(5, 101, "batter", True)
corpse = encounters(5, 101, "corpse", False)
gnasher = encounters(10, 101, "gnasher", True)
sorrow = encounters(10, 101, "sorrow", True)
shop = encounters(15, 101, "shop", False)
lore2 = encounters(15, 101, "lore2", False)
crow = encounters(15, 101, "crow", True)
stalker = encounters(15, 101, "stalker", False)
beelzebub = encounters(15, 50, "beelzebub", True)
blackcat = encounters(15, 101, "blackcat", False)
rest = encounters(15, 101, "rest", False)
mugging = encounters(15, 101, "mugging", False)
mansion = encounters(15, 101, "mansion", False)
doctor = encounters(15, 101, "doctor", False)
cult = encounters(17, 101, "cult", False)
altar = encounters(17, 101, "altar", False)
crawler = encounters(17, 101, "crawler", True)
mirror = encounters(17, 101, "mirror", False)
hunter = encounters(20, 101, "hunter", True)
mimic = encounters(20, 50, "mimic", True)
witch = encounters(20, 100, "witch", False)
lore3 = encounters(20, 101, "lore3", False)
fleshortcut = encounters(25, 101, "fleshortcut", False)
amalgam = encounters(35, 101, "amalgam", True)
angel = encounters(35, 101, "angel", False)
gods_calling = encounters(40, 50, "gods_calling", False)
maskedbase = encounters(40, 101, "maskedbase", False)
terror = encounters(40, 50, "terror", False)
savior = encounters (40, 101, "saviour", False)
doll = encounters(40, 101, "doll", True)
hydra = encounters(40, 101, "hydra", True)
skinwalker = encounters(40, 101, "skinwalker", True)
HAD = encounters(45, 101, "H.A.D", True)


#encounters = different events which can occur
eventable = [flavour, Nsaneflavour, itemfind, slime, zombie, shadow, lore1, shrine, amigara, batter, corpse, gnasher, sorrow, shop, lore2, stalker, beelzebub, blackcat, rest, mugging, mansion, doctor, cult, altar, hunter, crawler, mirror, mimic, witch, lore3, fleshortcut, amalgam, angel, gods_calling, maskedbase, terror, savior, doll, hydra, skinwalker, HAD]
validevents = []


start = input("Press enter to take a step forward ")
#Loop ends when the player reaches 50m, or when health, hunger or stamina reach 0.
#Will have loop end at max doom later
while distance < 50 and player[1] and player[2] and player[3] > 0:
    time.sleep(1)
   #Removes an item from the inventory if it's value is 0
    devmode = False
    if food <= 0 and "meat" in items:
        items.remove("meat")
    if bandage <= 0 and "bandages" in items:
        items.remove("bandages")
    if pills <= 0 and "pills" in items:
        items.remove("pills")
    if roids <= 0 and "steroids" in items:
        items.remove("steroids")
    if knives <= 0 and "knife" in items:
        items.remove("knife")
    if rbtfoot <= 0 and "rabbit foot" in items:
        items.remove("rabbit foot")
    if acid <= 0 and "acid" in items:
        items.remove("acid")

        
        
    print("")
    print("")
    print("")
    print("")
    print("")
    print("You have traveled", distance, "meters")
    print("Health:", str(player[1])+"/"+str(player[0]))
    print("Hunger:", player[2])
    print("Sanity:", player[3])
    print("Press A to look at items")
    progress = input("")
    progress = progress.upper()
    if progress == "D":
        print("DEBUG MODE ACTIVATED")
        print("")
        print("A: custom event")
        print("B: adjust values")
        x = input().lower()
        if x == "a":
            for i in range(len(eventable)):
                print(eventable[i].name)
            print("Which event would you like to try?")
            event = input()
            devmode = True
        elif x == "b":
            y = input("What value would you like to adjust?")
            if y == "distance":
                z = int(input("What is the new distance?"))
                distance = z

    elif progress == "A" and len(items) < 1:
        #prints gold amount and tells the player they have no items, then returns to start of loop
        print("You have", player[7], "gold")
        time.sleep(1.5)
        print("You have no items")
        time.sleep(1.5)
        continue
    elif progress == "A" and len(items) >= 1:
        print("You have", player[7], "gold")
        time.sleep(1.5)
        for i in range(len(items)):
            #prints a letter for each item in inventory eg: A,B,C,D,etc
            print((chr(i+65))+":", items[i])
        print(chr(len(items)+65)+":", "back")
        itemuse = input("")
        #turns letter input into a number, checks if number is in list
        if ord(itemuse.upper())-65 < len(items):
            x = items[ord(itemuse.upper())-65]
            if x == "meat":
                print("meat (consumable)")
                time.sleep(1.5)
                print("Restores 50 hunger")
                print("Don't ask where it's from")
                time.sleep(1.5)
                print("You have:", food)
                print("Consume the meat?")
                time.sleep(1.5)
                print("A: Yes")
                print("B: No")
                y = input()
                if y.lower() == "a":
                    print("You ate the meat")
                    player[2] += 50
                    if player[2] > 100:
                        player[2] = 100
                    food -= 1
                    if food == 0:
                        items.remove("meat")
        continue


  #Event start
    print("")
    print("")
    print("")
    print("")
    print("")
    print("You venture forth into the murky alleyways")
    if devmode == False:
        for i in range(len(eventable)):
            # adds the name of event to the validevents if the difficulty and sanity requirements are met.
            if distance >= eventable[i].diff and player[3] <= eventable[i].san:
                validevents.append(eventable[i].name)
        event = validevents[random.randint(0, len(validevents)-1)]
        time.sleep(2)


#Most events are just placeholder test to let me know if it's working
    if event == "flavour":
        print("Gloom and paranoia fill the air")

    elif event == "Nsaneflavour":
        print("insane event")

    elif event == "shadow":
        print("insane encounter: shadow")

    elif event == "slime":
        print("combat encounter: slime")

    elif event == "batter":
        print("combat encounter: masked man")

    elif event == "zombie":
        print("combat encounter: zombie")

    elif event == "amigara":
        print("Junji ito reference")
        distance += 2

    elif event == "lore1":
        print("Newspaper about new energy")

    elif event == "lore2":
        print("Scientist research paper")

    elif event == "lore3":
        print("Cult room")

    elif event == "gnasher":
        print("combat encounter: gnasher")

    elif event == "sorrow":
        print("combat encounter: sorrow")

    elif event == "itemfind":
        itempool = random.randint(1,100)
        if itempool + player[5] < 90:
            #normal drops
            itempool = random.randint(1,100)
            if itempool <= 25:
                print("You found some meat!")
                food += 1
                if "meat" in items == False:
                    items.append("meat")

            elif itempool <=50:
                print("You found some bandages!")
                bandage += 1
                if "bandages" in items == False:
                    items.append("bandages")

            elif itempool <= 75:
                print("You found some pills!")
                pills += 1
                if "pills" in items == False:
                    items.append("pills")

            elif itempool <= 100:
                print("You found some gold")
                player[7]+=1

        elif itempool + player[5] >= 90 and hasgun == False:
            itempool = random.randint(1,100)
            #rare drops (no gun)
            if itempool+player[5] <= 30:
                print("You found a knife!")
                knives += 1
                if "knife" in items == False:
                    items.append("knife")

            elif itempool+player[5] <= 55:
                print("You found a lucky charm!")
                charm += 1
                if "lucky charm" in items == False:
                    items.append("lucky charm")

            elif itempool+player[5] <= 75:
                print("You found some steroids!")
                roids += 1
                if "steroids" in items == False:
                    items.append("steroids")

            elif itempool+player[5] <= 90:
                print("You found a rabbit's foot!")
                rbtfoot += 1
                if "rabbit foot" in items == False:
                    items.append("rabbit foot")

            elif itempool+player[5] <= 100:
                print("You found a vial of acid!")
                acid += 1
                if "acid vial" in items == False:
                    items.append("acid vial")


        elif itempool + player[5] >= 90 and hasgun == True:
            itempool = random.randint(1,100)
            #rare drops (with gun)
            if itempool+player[5] <= 25:
                print("You found a knife!")
                knives += 1
                if "knife" in items == False:
                    items.append("knife")

            elif itempool+player[5] <= 45:
                print("You found some ammo!")
                ammo += 1

            elif itempool+player[5] <= 65:
                print("You found a lucky charm!")
                charm += 1
                if "lucky charm" in items == False:
                    items.append("lucky charm")

            elif itempool+player[5] <= 80:
                print("You found some steroids!")
                roids += 1
                if "steroids" in items == False:
                    items.append("steroids")

            elif itempool+player[5] <= 95:
                print("You found a rabbit's foot!")
                rbtfoot += 1
                if "rabbit foot" in items == False:
                    items.append("rabbit foot")

            elif itempool+player[5] <= 100:
                print("You found a vial of acid!")
                acid += 1
                if "acid vial" in items == False:
                    items.append("acid vial")




    elif event == "shrine":
        print("You find a shrine to a local diety")
        time.sleep(1.5)
        print("A: Offer some money")
        print("B: Offer some food")
        print("C: Loot the shrine")
        print("D: move on")
        shrine = input().lower()
        if shrine == "a":
            print("how much money will you offer?")
            a = int(input())
            if a <= 0:
                print("You change your mind")
            elif a > player[7]:
                print("You don't have enough money!")
            else:
                player[7] -= a
                player[5] += a
                print("You offer", a, "gold to the shrine")
                time.sleep(1.5)
                print("You feel blessed")
                time.sleep(1)
                print("[Luck +"+str(a)+"]")
        elif shrine == "b":
            if food > 0:
                print("How much food will you offer?")
                a = int(input())
                if a > food:
                    print("You don't have enough food!")
                elif a <= 0:
                    print("You change your mind")
                else:
                    food -= a
                    player[5] += a
                    print("You offer some food to the shrine")
                    time.sleep(1.5)
                    print("You feel blessed")
                    time.sleep(1)
                    print("[Luck +"+str(a)+"]")
        elif shrine == "c":
            print("Nobody's gonna care if you take a few things right?")
            time.sleep(1)
            print("Besides, you need these supplies more than some nonexistant gods")
            time.sleep(1.5)
            print("[Gold +1]")
            time.sleep(1)
            print("As you leave, you are suddenly assaulted by a wave of regret")
            time.sleep(1.5)
            print("You feel damned")
            time.sleep(1)
            print("[Luck -1]")

    elif event == "drink":
        print("You have been walking for a long time, and you find yourself in dire need of water")
        time.sleep(1.5)
        print("Ahead of you, you spot an old faucet connected to a wall.")
        time.sleep(1.5)
        print("Drink from the faucet?")
        time.sleep(1)
        print("A: Yes")
        print("B: No")
        x = input().lower()
        if x == "a":
            print("You turn the faucet")
            time.sleep(2)
            if skillcheck(player[5], 50) == True:
                print("Cool, refreshing water flows down the tap, revitalising your body and mind")
                time.sleep(1.5)
                print("[Sanity +10]")
                player[3] += 10
                if player[3] > 100:
                    player[3] = 100
            else:
                print("The faucet turns on, but it doesn't produce water")
                time.sleep(1.5)
                print("Instead, blood flows down, coating your hands and feet")
                time.sleep(1.5)
                print("[Sanity -10]")
                player[3] -= 10
        else:
            print("You decide to ignore it, the water isn't safe.")
            time.sleep(1.5)
            print("But your thirst has become dire, and you find yourself growing weaker because of it")
            time.sleep(1.5)
            if player[4] -1 == 0:
                print("[Health -1]")
                player[1] -= 1
            else:
                print("[Attack -1]")
                player[4] -= 1

    elif event == "mansion":
        print("Mansion event")

    elif event == "altar":
        print("You come across a mysterious altar")
        time.sleep(1.5)
        print("You hear voices calling to you, inviting you to join them")
        time.sleep(2)
        if skillcheck(player[5], 50) == True:
            print()
            print("You resist the voices and press on")
        else:
            print()
            print("Your mind wavers, as you feel yourself losing your grip on reality")
            time.sleep(1)
            print("[Sanity -50]")
            player[3] -= 50

    elif event == "shop":
        print("Shop")

    elif event == "witch":
        print("Witch")

    elif event == "stalker":
        print("You feel as though you are being watched")
        stalking = 3

    elif event == "crow":
        print("combat encounter: crow")

    elif event == "mirror":
        print("You look in the mirror")
        time.sleep(1.5)
        if player[3] < 50:
            print("insane encounter: mimic")
        elif skillcheck(player[5], 70) == True:
            print("It's you")
        else:
            print("That's not you")
            time.sleep(1)
            print("[Sanity -10]")
            player[3] -= 10

    elif event == "mimic":
        print("insane encounter: mimic")

    elif event == "beelzebub":
        print("insane encounter: beelzebub")

    elif event == "hunter":
        print("combat encounter: hunter")

    elif event == "crawler":
        print("combat encounter: crawler")

    elif event == "blackcat":
        print("You find a small black cat lying in front of you")
        time.sleep(1.5)
        print("It looks at you and lets out a small meow")
        time.sleep(1.5)
        print("A: pet the cat")
        print("B: consume")
        x = input()
        x = x.lower()
        if x == "a":
            print("You bend down and gently stroke the cat as it climbs into your lap")
            time.sleep(1.5)
            print("The act soothes you, reminding you of the small good that still exists in this hostile world.")
            time.sleep(1.5)
            print("[Sanity +50]")
            player[3] = player[3]+50
            if player[3] > 100:
                player[3] = 100
            time.sleep(1)
            print("Satisfied, the cat scampers off into the darkness")
            time.sleep(1.5)
            print("What was that saying about black cats again?")
            time.sleep(1)
            print("[Luck -1]")

        else:
            print("Though it breaks your heart, the cat is easy prey. If you give up on this opportunity, who knows when your next meal will be?")
            time.sleep(1.5)
            print("Sneaking up on the cat, you strike it.")
            time.sleep(1)
            print("Again")
            time.sleep(1)
            print("And again")
            time.sleep(1)
            print("And again")
            time.sleep(1.5)
            print("You can barely look at the kitten as you tear into it, your meal tainted with the taste of regret")
            time.sleep(1.5)
            print("[Hunger +30]")
            player[2] = player[2] + 30
            if player[2] > 100:
                player[2] = 100
            print("[Sanity -50]")
            player[3]-= 50

    elif event == "rest":
        print("Rest space")

    elif event == "doctor":
        print("You encounter a man in a bloodstained doctor's uniform")
        time.sleep(1.5)
        print("He shambles towards you, pulling down his mask to reveal a crooked row of yellow teeth fixed in a menacing grin")
        time.sleep(1.5)
        print("'Ah, a healthy donor! It's been so long since I've had someone like you.'")
        time.sleep(1.5)
        print("'Please, won't you consider donating your blood for those in need? There are many dying patients who could use it much more than you, and I'll offer a reward too!'")
        time.sleep(1.5)
        print("The doctor raises a long rusted needle, covered in bits of dried blood")
        time.sleep(1.5)
        print("Accept the", "doctor's", "request?")
        time.sleep(1)
        print("A: Yes")
        print("B: No way!")
        x = input()
        x = x.lower()
        if x == "a":
            print("The doctor jabs the needle into your arm with the care and grace of an enraged bull")
            time.sleep(1.5)
            print("Blood spurts out of your arm with vigor, as the doctor produces a bottle and flails around trying to catch it all")
            time.sleep(1.5)
            print("The sight and amount of  blood leaving your body makes you dizzy, and you find yourself losing consciousness")
            time.sleep(1.5)
            print("[Health -2]")
            time.sleep(1.5)
            print("When you come to, the doctor stands before you, an empty bottle clutched in his hands")
            time.sleep(1.5)
            print("'Well unfortunately we were not able to collect much blood this time round, but a deal is a deal so I shall give you your compensation'")
            time.sleep(1.5)
            print("The doctor bends over and hands you 2 gold")
            time.sleep(1.5)
            print("You see a red liquid trickle down the corner of the doctor's mouth, which he quickly licks up")
            time.sleep(1.5)
            print("Anyway, I hope you come again, many patients are counting on your blood, we simply MUST have it!")

        else:
            print("You turn to leave, you already have yourself to worry about")
            time.sleep(1.5)
            print("Suddenly, your arm is grasped by the doctor's!")
            time.sleep(1.5)
            print("'Oh I don't think so. Your blood is simply to precious for us to give up!'")
            time.sleep(1.5)
            if skillcheck(player[5], 50) == True:
                print("You manage to pull free of the mad doctor's grasp and escape")
            else:
                print("The doctor stabs the needle deep into your arm, with no regard for proper procedure")
                time.sleep(1.5)
                print("[Health -2]")
                player[1] = player[1]-2
                time.sleep(1.5)
                print("Blood gushes out of your arm, which the doctor messily tries to collect in a bottle")
                time.sleep(1.5)
                print("Using your other hand, you close your fist around the needle and yank it out, ignoring the searing pain")
                time.sleep(1.5)
                print("You then bring it down with all your might on the doctor's arm, who releases his grip, suprised.")
                time.sleep(1.5)
                print("As he stumbles back in surprise, you seize the opportunity to escape.")

    elif event == "fleshortcut":
        print("Flesh shortcut")

    elif event == "amalgam":
        print("combat encounter: amalgam")

    elif event == "mugging":
        print("Mugging")

    elif event == "cult":
        print("Cult")

    elif event == "angel":
        print("insane encounter: angel")

    elif event == "gods_calling":
        print("You hear the voices of the old ones calling to you")
        time.sleep(1.5)
        x = 2
        for i in range(50):
            print("S̷̗̪̆͗U̷͓̚͝F̷̲̒F̷̩͕̄̕Ḙ̷̡͠R̶͖̂ ̸̹̗̂F̷̮̦͝O̷̰̎R̴̡̖̃ ̴̳̓̓Ṁ̴̹͍E̷̠͌ͅ")
            time.sleep(x)
            x /= 1.5
        t_end = time.time() + 1
        while time.time() < t_end:
            print("S̷̗̪̆͗U̷͓̚͝F̷̲̒F̷̩͕̄̕Ḙ̷̡͠R̶͖̂ ̸̹̗̂F̷̮̦͝O̷̰̎R̴̡̖̃ ̴̳̓̓Ṁ̴̹͍E̷̠͌ͅ")
        if skillcheck(player[5], 50) == True:
            print("You cast  them out of your head and press on")
            time.sleep(1.5)
            print("You won't let them try to control you anymore")
            time.sleep(1.5)
            print("Sanity fully restored")
            player[3] = 100
        else:
            if "knife" in items:
                print("You shakily draw a knife and plunge it into your stomach")
                time.sleep(1.5)
                print("Health -" + str(player[4]))
                player[1] -= player[4]

            else:
                print("You gouge out your own eyes")

    elif event == "hydra":
        print("combat encounter: hydra")

    elif event == "skinwalker":
        print("combat encounter: skinwalker")

    elif event == "saviour":
        print("person being attacked")

    elif event == "maskedbase":
        print("You come across a base of masked men. The one in the centre seems to be the leader")

    elif event == "doll":
        print("combat encounter: doll")

    elif event == "terror":
        print("insane encounter: terror")

    elif event == "H.A.D":
        print("combat encounter: H.A.D")


    distance += 1
    player[2] -= 10



if distance >= 50:
    print("You made it!")
    
elif player[2] <= 0:
    print("Your hunger has grown too great and cannot be ignored any longer")
    time.sleep(1)
    print("Collapsing onto the ground, the world grows distant as you starve to death")
    time.sleep(1)
    print("GAME OVER")
    
elif player[3] <= 0:
    print("You have completely gone insane")
    time.sleep(1)
    print("Shadows and hallucinations dance in front of you as reality crumbles")
    time.sleep(1)
    print("A giant hand slowly extends towards you, but you find yourself in no position to stop it")
    time.sleep(1)
    print("From this day on, your body no longer belongs to you.")
    time.sleep(1)
    print("GAME OVER")
