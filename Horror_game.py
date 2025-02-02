import random
import time
from encounters import eventable
from  parameters import v0, v, inv, items
from character_sheets import maxhealth, health, hunger, sanity, doom, atk, luck, accuracy, xp, gold


#Values are the stat you want changed, the amount it changes by, and the amount it changes by under DOOM




#Function used when an event has a random outcome
def skillcheck(luck, minnumber):
#minnumber is the percentage chance of success. 75% = (minnumber = 75)
    if (random.randint(1, 100) - luck) <= minnumber:
        return True
    else:
        return False


validevents = []



start = input("Press enter to take a step forward ")
#Loop ends when the player reaches 50m, or when health, hunger or stamina reach 0.
#Will have loop end at max doom later
while v0.distance < 50 and health > 0 and hunger > 0 and sanity > 0:
    time.sleep(v.Swait)
   #Removes an item from the inventory if it's value is 0
    devmode = False
    if inv.food <= 0 and "meat" in items:
        items.remove("meat")
    if inv.bandage <= 0 and "bandages" in items:
        items.remove("bandages")
    if inv.pills <= 0 and "pills" in items:
        items.remove("pills")
    if inv.roids <= 0 and "steroids" in items:
        items.remove("steroids")
    if inv.knives <= 0 and "knife" in items:
        items.remove("knife")
    if inv.rbtfoot <= 0 and "rabbit foot" in items:
        items.remove("rabbit foot")
    if inv.acid <= 0 and "acid" in items:
        items.remove("acid")

        
        
    print("")
    print("")
    print("")
    print("")
    print("")
    print("You have traveled", v0.distance, "meters")
    print("Health:", str(health)+"/"+str(maxhealth))
    print("Hunger:", hunger)
    print("Sanity:", sanity)
    print("Press A to look at items")
    progress = input("")
    if progress == "^^vv<><>BAstart":
        x = input("DEBUG MODE ACTIVATED\nA: custom event\nB: adjust values\nC: speed up\n").lower()
        if x == "a":
            for i in range(len(eventable)):
                print(eventable[i].name)
            print("Which event would you like to try?")
            event = input()
            devmode = True
        elif x == "b":
            y = input("What value would you like to adjust?\n")
            if y == "distance":
                z = int(input("What is the new distance?\n"))
                v0.distance = z
                continue
        elif x == "c":
            print("SPEED UP!\nSPEED UP!\nSPEED UP!")
            v.Swait = 0
            v.Mwait = 0.5
            v.Lwait = 1
            continue

    elif progress == "A" and len(items) < 1:
        #prints gold amount and tells the player they have no items, then returns to start of loop
        print("You have", gold, "gold")
        time.sleep(v.Mwait)
        print("You have no items")
        time.sleep(v.Mwait)
        continue
    elif progress == "A" and len(items) >= 1:
        print("You have", gold, "gold")
        time.sleep(v.Mwait)
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
                time.sleep(v.Mwait)
                print("Restores", v.largerestore, "hunger")
                print("Don't ask where it's from")
                time.sleep(v.Mwait)
                print("You have:", inv.food)
                print("Consume the meat?")
                time.sleep(v.Mwait)
                print("A: Yes")
                print("B: No")
                y = input()
                if y.lower() == "a":
                    print("You ate the meat")
                    hunger += v.largerestore
                    if hunger > 100:
                        hunger = 100
                    inv.food -= 1
                    if inv.food == 0:
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
            if v0.distance >= eventable[i].diff and sanity <= eventable[i].san:
                validevents.append(eventable[i].name)
        event = validevents[random.randint(0, len(validevents)-1)]
        time.sleep(v.Lwait)


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

    elif event == "lootcorpse":
        print("Do you loot the corpse? 25% chance zombie, add 25% chance skinwalker diff > 30")

    elif event == "amigara":
        print("Junji ito reference")
        v0.distance += 2

    elif event == "lore1":
        print("Newspaper about new energy")

    elif event == "lore2":
        print("Scientist research paper")

    elif event == "lore3":
        print("Cult room")

    elif event == "konami":
        print("You see some writing etched onto a wall")
        time.sleep(v.Mwait)
        print('It reads "^^vv<><>BA"')
        code = ["^", "^", "v", "v", "<",">", "<", ">"]
        fail = False
        codewords = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth"]
        time.sleep(v.Mwait)
        print("These seem to be the moves to an ancient counteritual to stop the apocalypse")
        time.sleep(v.Mwait)
        print("Perform the ritual?")
        time.sleep(v.Swait)
        print("A: Yes")
        print("B: No")
        x = input().lower()
        if x == "a":
            for i in range(25):
                print("\n")
            for i in range(8):
                dance = input("Please enter the "+ codewords[i]+ " move of the ritual\n")


                if dance == code[i]:
                    continue
                else:
                    fail = True
                    break
            if fail == False:
                print("Is that all?")
                time.sleep(v.Swait)
                print("A: Yes")
                dance = input("B: No\n")
                if dance == "B":
                    print("What about now?")
                    time.sleep(v.Swait)
                    print("A: Yes")
                    dance = input("B: No\n")
                    if dance == "A":
                        print("You completed the ritual")
                        time.sleep(v.Swait)
                        print("D00M -" +str(v.smallschange)+"]")
                        Doom -= v.v.smallchange

                    else:
                        fail = True
                else:
                    fail = True

            if fail == True:
                print("You failed the ritual")
                time.sleep(v.Swait)
                print("D00M +" +str(v.smallschange)+"]")
                Doom += v.smallchange


        else:
            print("You aren't going to make a fool of yourself trying to do some ridiculous dance")
            time.sleep(v.Swait)
            print("Besides, it probably wouldn't have worked anyway")


    elif event == "deersac":
        print("You see a young fawn strapped to an altar")

    elif event == "taxes":
        print("The buildings begin to twist and distort themselves the further you go")
        time.sleep(v.Mwait)
        print("The rough tarmak of the streets slowly becomes replaced with soft, clumpy dirt")
        time.sleep(v.Mwait)
        print("")

    elif event == "gnasher":
        print("combat encounter: gnasher")

    elif event == "sorrow":
        print("combat encounter: sorrow")

    elif event == "meat":
        print("You found some meat!")
        inv.food += 1
        if "meat" in items == False:
            items.append("meat")

    elif event == "bandages":
        print("You found some bandages!")
        inv.bandage += 1
        if "bandages" in items == False:
            items.append("bandages")

    elif event == "pills":
        print("You found some pills!")
        inv.pills += 1
        if "pills" in items == False:
            items.append("pills")

    elif event == "gold":
        print("You found some gold")
        gold += 1

    elif event == "itemfind":
        if v0.hasgun == False:
            itempool = random.randint(1,100)
            #rare drops (no gun)
            if itempool+luck <= 20:
                print("You found a knife!")
                inv.knives += 1
                if "knife" in items == False:
                    items.append("knife")

            elif itempool+luck <= 40:
                print("You found an effigy!")
                inv.effigy += 1
                if "effigy" in items == False:
                    items.append("effigy")

            elif itempool+luck <= 60:
                print("You found a lucky charm!")
                inv.charm += 1
                if "lucky charm" in items == False:
                    items.append("lucky charm")

            elif itempool+luck <= 80:
                print("You found some steroids!")
                inv.roids += 1
                if "steroids" in items == False:
                    items.append("steroids")

            elif itempool+luck <= 90:
                print("You found a rabbit's foot!")
                inv.rbtfoot += 1
                if "rabbit foot" in items == False:
                    items.append("rabbit foot")

            elif itempool+luck <= 100:
                print("You found a vial of acid!")
                inv.acid += 1
                if "acid vial" in items == False:
                    items.append("acid vial")


        elif itempool + luck >= 90 and v0.hasgun == True:
            itempool = random.randint(1,100)
            #rare drops (with gun)
            if itempool+luck <= 25:
                print("You found a knife!")
                inv.knives += 1
                if "knife" in items == False:
                    items.append("knife")

            elif itempool+luck <= 45:
                print("You found some ammo!")
                inv.ammo += 1

            elif itempool+luck <= 65:
                print("You found a lucky charm!")
                inv.charm += 1
                if "lucky charm" in items == False:
                    items.append("lucky charm")

            elif itempool+luck <= 80:
                print("You found some steroids!")
                inv.roids += 1
                if "steroids" in items == False:
                    items.append("steroids")

            elif itempool+luck <= 95:
                print("You found a rabbit's foot!")
                inv.rbtfoot += 1
                if "rabbit foot" in items == False:
                    items.append("rabbit foot")

            elif itempool+luck <= 100:
                print("You found a vial of acid!")
                inv.acid += 1
                if "acid vial" in items == False:
                    items.append("acid vial")

    elif event == "tunnelchase":
        print("tunnelchase")


    elif event == "shrine":
        print("You find a shrine to a local diety")
        time.sleep(v.Mwait)
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
            elif a > gold:
                print("You don't have enough money!")
            else:
                gold -= a
                luck += a
                print("You offer", a, "gold to the shrine")
                time.sleep(v.Mwait)
                print("You feel blessed")
                time.sleep(v.Swait)
                print("[Luck +"+str(a)+"]")
        elif shrine == "b":
            if inv.food > 0:
                print("How much food will you offer?")
                a = int(input())
                if a > inv.food:
                    print("You don't have enough food!")
                elif a <= 0:
                    print("You change your mind")
                else:
                    inv.food -= a
                    luck += a
                    print("You offer some food to the shrine")
                    time.sleep(v.Mwait)
                    print("You feel blessed")
                    time.sleep(v.Swait)
                    print("[Luck +"+str(a)+"]")
        elif shrine == "c":
            print("Nobody's gonna care if you take a few things right?")
            time.sleep(v.Swait)
            print("Besides, you need these supplies more than some nonexistant gods")
            time.sleep(v.Mwait)
            print("[Gold +" + str(v.smallschange)+"]")
            gold += v.smallschange
            time.sleep(v.Swait)
            print("As you leave, you are suddenly assaulted by a wave of regret")
            time.sleep(v.Mwait)
            print("You feel damned")
            time.sleep(v.Swait)
            print("[Luck -"+str(v.smallschange)+"]")
            luck -= v.smallschange

    elif event == "drink":
        print("You have been walking for a long time, and you find yourself in dire need of water")
        time.sleep(v.Mwait)
        print("Ahead of you, you spot an old faucet connected to a wall.")
        time.sleep(v.Mwait)
        print("Drink from the faucet?")
        time.sleep(v.Swait)
        print("A: Yes")
        print("B: No")
        x = input().lower()
        if x == "a":
            print("You turn the faucet")
            time.sleep(v.Lwait)
            if skillcheck(luck, 50) == True:
                print("Cool, refreshing water flows down the tap, revitalising your body and mind")
                time.sleep(v.Mwait)
                print("[Sanity +" + str(v.v.smallchange)+"]")
                sanity += v.v.smallchange
                if sanity > 100:
                    sanity = 100
            else:
                print("The faucet turns on, but it doesn't produce water")
                time.sleep(v.Mwait)
                print("Instead, blood flows down, coating your hands and feet")
                time.sleep(v.Mwait)
                print("[Sanity -"+str(v.v.smallchange)+"]")
                sanity -= v.v.smallchange
        else:
            print("You decide to ignore it, the water isn't safe.")
            time.sleep(v.Mwait)
            print("But your thirst has become dire, and you find yourself growing weaker because of it")
            time.sleep(v.Mwait)
            print("[Health -"+str(v.smallschange)+"]")
            health -= v.smallschange


    elif event == "mansion":
        print("Mansion event")

    elif event == "altar":
        print("You come across a mysterious altar")
        time.sleep(v.Mwait)
        print("You hear voices calling to you, inviting you to join them")
        time.sleep(v.Lwait)
        if skillcheck(luck, 50) == True:
            print()
            print("You resist the voices and press on")
        else:
            print()
            print("Your mind wavers, as you feel yourself losing your grip on reality")
            time.sleep(v.Swait)
            print("[Sanity -50]")
            sanity -= 50

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
        time.sleep(v.Mwait)
        if sanity < 50:
            print("insane encounter: mimic")
        elif skillcheck(luck, 70) == True:
            print("It's you")
        else:
            print("That's not you")
            time.sleep(v.Swait)
            print("[Sanity -" + str(v.v.smallchange)+"]")
            sanity -= v.v.smallchange

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
        time.sleep(v.Mwait)
        print("It looks at you and lets out a small meow")
        time.sleep(v.Mwait)
        print("A: pet the cat")
        print("B: consume")
        x = input()
        x = x.lower()
        if x == "a":
            print("You bend down and gently stroke the cat as it climbs into your lap")
            time.sleep(v.Mwait)
            print("The act soothes you, reminding you of the small good that still exists in this hostile world.")
            time.sleep(v.Mwait)
            print("[Sanity +50]")
            sanity = sanity+50
            if sanity > 100:
                sanity = 100
            time.sleep(v.Swait)
            print("Satisfied, the cat scampers off into the darkness")
            time.sleep(v.Mwait)
            print("What was that saying about black cats again?")
            time.sleep(v.Swait)
            print("[Luck -" +str(v.smallschange)+"]")
            luck -= v.smallschange

        else:
            print("Though it breaks your heart, the cat is easy prey. If you give up on this opportunity, who knows when your next meal will be?")
            time.sleep(v.Mwait)
            print("Sneaking up on the cat, you strike it.")
            time.sleep(v.Swait)
            print("Again")
            time.sleep(v.Swait)
            print("And again")
            time.sleep(v.Swait)
            print("And again")
            time.sleep(v.Mwait)
            print("You can barely look at the kitten as you tear into it, your meal tainted with the taste of regret")
            time.sleep(v.Mwait)
            print("[Hunger +"+str(v.smallrestore)+"]")
            hunger = hunger + v.smallrestore
            if hunger > 100:
                hunger = 100
            print("[Sanity -50]")
            sanity -= 50

    elif event == "rest":
        print("Rest space")

    elif event == "doctor":
        print("You encounter a man in a bloodstained doctor's uniform")
        time.sleep(v.Mwait)
        print("He shambles towards you, pulling down his mask to reveal a crooked row of yellow teeth fixed in a menacing grin")
        time.sleep(v.Mwait)
        print("'Ah, a healthy donor! It's been so long since I've had someone like you.'")
        time.sleep(v.Mwait)
        print("'Please, won't you consider donating your blood for those in need? There are many dying patients who could use it much more than you, and I'll offer a reward too!'")
        time.sleep(v.Mwait)
        print("The doctor raises a long rusted needle, covered in bits of dried blood")
        time.sleep(v.Mwait)
        print("Accept the", "doctor's", "request?")
        time.sleep(v.Swait)
        print("A: Yes")
        print("B: No way!")
        x = input()
        x = x.lower()
        if x == "a":
            print("The doctor jabs the needle into your arm with the care and grace of an enraged bull")
            time.sleep(v.Mwait)
            print("Blood spurts out of your arm with vigor, as the doctor produces a bottle and flails around trying to catch it all")
            time.sleep(v.Mwait)
            print("The sight and amount of  blood leaving your body makes you dizzy, and you find yourself losing consciousness")
            time.sleep(v.Mwait)
            print("[Health -"+str(v.largeschange)+"]")
            time.sleep(v.Mwait)
            print("When you come to, the doctor stands before you, an empty bottle clutched in his hands")
            time.sleep(v.Mwait)
            print("'Well unfortunately we were not able to collect much blood this time round, but a deal is a deal so I shall give you your compensation'")
            time.sleep(v.Mwait)
            print("The doctor bends over and hands you 2 gold")
            time.sleep(v.Mwait)
            print("You see a red liquid trickle down the corner of the doctor's mouth, which he quickly licks up")
            time.sleep(v.Mwait)
            print("Anyway, I hope you come again, many patients are counting on your blood, we simply MUST have it!")

        else:
            print("You turn to leave, you already have yourself to worry about")
            time.sleep(v.Mwait)
            print("Suddenly, your arm is grasped by the doctor's!")
            time.sleep(v.Mwait)
            print("'Oh I don't think so. Your blood is simply to precious for us to give up!'")
            time.sleep(v.Mwait)
            if skillcheck(luck, 50) == True:
                print("You manage to pull free of the mad doctor's grasp and escape")
            else:
                print("The doctor stabs the needle deep into your arm, with no regard for proper procedure")
                time.sleep(v.Mwait)
                print("[Health -" + str(v.largeschange) + "]")
                health -= v.largeschange
                time.sleep(v.Mwait)
                print("Blood gushes out of your arm, which the doctor messily tries to collect in a bottle")
                time.sleep(v.Mwait)
                print("Using your other hand, you close your fist around the needle and yank it out, ignoring the searing pain")
                time.sleep(v.Mwait)
                print("You then bring it down with all your might on the doctor's arm, who releases his grip, suprised.")
                time.sleep(v.Mwait)
                print("As he stumbles back in surprise, you seize the opportunity to escape.")

    elif event == "sacrifice":
        print("Choice to sacrifice health for a chance to raise stats. Raises doom")

    elif event == "fleshortcut":
        print("Flesh shortcut")

    elif event == "trap":
        print("50% chance for item, or take 3 damage")

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
        time.sleep(v.Mwait)
        x = v.Lwait
        for i in range(50):
            print("S̷̗̪̆͗U̷͓̚͝F̷̲̒F̷̩͕̄̕Ḙ̷̡͠R̶͖̂ ̸̹̗̂F̷̮̦͝O̷̰̎R̴̡̖̃ ̴̳̓̓Ṁ̴̹͍E̷̠͌ͅ")
            time.sleep(x)
            x /= v.Mwait
        t_end = time.time() + 1
        while time.time() < t_end:
            print("S̷̗̪̆͗U̷͓̚͝F̷̲̒F̷̩͕̄̕Ḙ̷̡͠R̶͖̂ ̸̹̗̂F̷̮̦͝O̷̰̎R̴̡̖̃ ̴̳̓̓Ṁ̴̹͍E̷̠͌ͅ")
        if skillcheck(luck, 50) == True:
            print("You cast  them out of your head and press on")
            time.sleep(v.Mwait)
            print("You won't let them try to control you anymore")
            time.sleep(v.Mwait)
            print("Sanity fully restored")
            Sanity = 100
        else:
            print("You shakily draw a knife and plunge it into your stomach")
            time.sleep(v.Mwait)
            print("[Health -" +str(atk) +"]")
            health -= atk

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


    v0.distance += 1
    hunger -= v.smallchange



if v0.distance >= 50:
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