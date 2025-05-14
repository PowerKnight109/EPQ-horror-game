       #Most events are just placeholder test to let me know if it's working
       # if event == "flavour":
            print("Gloom and paranoia fill the air")

      #  elif event == "Nsaneflavour":
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
            misc.distance += 2

        elif event == "lore1":
            print("Newspaper about new energy")

        elif event == "lore2":
            print("Scientist research paper")

        elif event == "lore3":
            print("Cult room")

        elif event == "konami":
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
                    dance = input("Please enter the " + codewords[i] + " move of the ritual\n")

                    if dance == code[i]:
                        continue
                    else:
                        fail = True
                        break
                if fail == False:
                    print("Is that all?")
                    time.sleep(para.Swait)
                    print("A: Yes")
                    dance = input("B: No\n")
                    if dance == "B":
                        print("What about now?")
                        time.sleep(para.Swait)
                        print("A: Yes")
                        dance = input("B: No\n")
                        if dance == "A":
                            print("You completed the ritual")
                            time.sleep(para.Swait)
                            print("D00M -" + str(para.smallschange) + "]")
                            Doom -= para.v.smallchange

                        else:
                            fail = True
                    else:
                        fail = True

                if fail == True:
                    print("You failed the ritual")
                    time.sleep(para.Swait)
                    print("D00M +" + str(para.smallschange) + "]")
                    Doom += para.smallchange


            else:
                print("You aren't going to make a fool of yourself trying to do some ridiculous dance")
                time.sleep(para.Swait)
                print("Besides, it probably wouldn't have worked anyway")


        elif event == "deersac":
            print("You see a young fawn strapped to an altar")

        elif event == "taxes":
            print("The buildings begin to twist and distort themselves the further you go")
            time.sleep(para.Mwait)
            print("The rough tarmak of the streets slowly becomes replaced with soft, clumpy dirt")
            time.sleep(para.Mwait)
            print("")

        elif event == "gnasher":
            print("combat encounter: gnasher")

        elif event == "sorrow":
            print("combat encounter: sorrow")

        elif event == "meat":
            print("You found some meat!")
            player.inv("meat") += 1
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
            player.gold += 1

        elif event == "itemfind":
            if misc.hasgun == False:
                itempool = random.randint(1, 100)
                #rare drops (no gun)
                if itempool + player.luck <= 20:
                    print("You found a knife!")
                    inv.knives += 1
                    if "knife" in items == False:
                        items.append("knife")

                elif itempool + player.luck <= 40:
                    print("You found an effigy!")
                    inv.effigy += 1
                    if "effigy" in items == False:
                        items.append("effigy")

                elif itempool + player.luck <= 60:
                    print("You found a lucky charm!")
                    inv.charm += 1
                    if "lucky charm" in items == False:
                        items.append("lucky charm")

                elif itempool + player.luck <= 80:
                    print("You found some steroids!")
                    inv.roids += 1
                    if "steroids" in items == False:
                        items.append("steroids")

                elif itempool + player.luck <= 90:
                    print("You found a rabbit's foot!")
                    inv.rbtfoot += 1
                    if "rabbit foot" in items == False:
                        items.append("rabbit foot")

                elif itempool + player.luck <= 100:
                    print("You found a vial of acid!")
                    inv.acid += 1
                    if "acid vial" in items == False:
                        items.append("acid vial")


            elif itempool + player.luck >= 90 and misc.hasgun == True:
                itempool = random.randint(1, 100)
                #rare drops (with gun)
                if itempool + player.luck <= 25:
                    print("You found a knife!")
                    inv.knives += 1
                    if "knife" in items == False:
                        items.append("knife")

                elif itempool + player.luck <= 45:
                    print("You found some ammo!")
                    inv.ammo += 1

                elif itempool + player.luck <= 65:
                    print("You found a lucky charm!")
                    inv.charm += 1
                    if "lucky charm" in items == False:
                        items.append("lucky charm")

                elif itempool + player.luck <= 80:
                    print("You found some steroids!")
                    inv.roids += 1
                    if "steroids" in items == False:
                        items.append("steroids")

                elif itempool + player.luck <= 95:
                    print("You found a rabbit's foot!")
                    inv.rbtfoot += 1
                    if "rabbit foot" in items == False:
                        items.append("rabbit foot")

                elif itempool + player.luck <= 100:
                    print("You found a vial of acid!")
                    inv.acid += 1
                    if "acid vial" in items == False:
                        items.append("acid vial")

        elif event == "tunnelchase":
            print("tunnelchase")


        elif event == "shrine":
            print("You find a shrine to a local diety")
            time.sleep(para.Mwait)
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
                if inv.food > 0:
                    print("How much food will you offer?")
                    a = int(input())
                    if a > inv.food:
                        print("You don't have enough food!")
                    elif a <= 0:
                        print("You change your mind")
                    else:
                        inv.food -= a
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

        elif event == "drink":
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
                if skillcheck(player.luck, 50) == True:
                    print("Cool, refreshing water flows down the tap, revitalising your body and mind")
                    time.sleep(para.Mwait)
                    print("[Sanity +" + str(para.v.smallchange) + "]")
                    sanity += para.v.smallchange
                    if sanity > 100:
                        sanity = 100
                else:
                    print("The faucet turns on, but it doesn't produce water")
                    time.sleep(para.Mwait)
                    print("Instead, blood flows down, coating your hands and feet")
                    time.sleep(para.Mwait)
                    print("[Sanity -" + str(para.v.smallchange) + "]")
                    sanity -= para.v.smallchange
            else:
                print("You decide to ignore it, the water isn't safe.")
                time.sleep(para.Mwait)
                print("But your thirst has become dire, and you find yourself growing weaker because of it")
                time.sleep(para.Mwait)
                print("[Health -" + str(para.smallschange) + "]")
                player.health -= para.smallschange


        elif event == "mansion":
            print("Mansion event")

        elif event == "altar":
            print("You come across a mysterious altar")
            time.sleep(para.Mwait)
            print("You hear voices calling to you, inviting you to join them")
            time.sleep(para.Lwait)
            if skillcheck(player.luck, 50) == True:
                print()
                print("You resist the voices and press on")
            else:
                print()
                print("Your mind wavers, as you feel yourself losing your grip on reality")
                time.sleep(para.Swait)
                print("[Sanity -30]")
                player.sanity -= 30

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
            time.sleep(para.Mwait)
            if sanity < 50:
                print("insane encounter: mimic")
            elif skillcheck(player.luck, 70) == True:
                print("It's you")
            else:
                print("That's not you")
                time.sleep(para.Swait)
                print("[Sanity -" + str(para.v.smallchange) + "]")
                sanity -= para.v.smallchange

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
            time.sleep(para.Mwait)
            print("It looks at you and lets out a small meow")
            time.sleep(para.Mwait)
            print("A: pet the cat")
            print("B: consume")
            x = input()
            x = x.lower()
            if x == "a":
                print("You bend down and gently stroke the cat as it climbs into your lap")
                time.sleep(para.Mwait)
                print("The act soothes you, reminding you of the small good that still exists in this hostile world.")
                time.sleep(para.Mwait)
                print("[Sanity +50]")
                sanity = sanity + 50
                if sanity > 100:
                    sanity = 100
                time.sleep(para.Swait)
                print("Satisfied, the cat scampers off into the darkness")
                time.sleep(para.Mwait)
                print("What was that saying about black cats again?")
                time.sleep(para.Swait)
                print("[Luck -" + str(para.smallschange) + "]")
                player.luck -= para.smallschange

            else:
                print(
                    "Though it breaks your heart, the cat is easy prey. If you give up on this opportunity, who knows when your next meal will be?")
                time.sleep(para.Mwait)
                print("Sneaking up on the cat, you strike it.")
                time.sleep(para.Swait)
                print("Again")
                time.sleep(para.Swait)
                print("And again")
                time.sleep(para.Swait)
                print("And again")
                time.sleep(para.Mwait)
                print(
                    "You can barely look at the kitten as you tear into it, your meal tainted with the taste of regret")
                time.sleep(para.Mwait)
                print("[Hunger +" + str(para.smallrestore) + "]")
                player.hunger = player.hunger + para.smallrestore
                if player.hunger > 100:
                    player.hunger = 100
                print("[Sanity -50]")
                sanity -= 50

        elif event == "rest":
            print("Rest space")

        elif event == "doctor":
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
                if skillcheck(player.luck, 50) == True:
                    print("You manage to pull free of the mad doctor's grasp and escape")
                else:
                    print("The doctor stabs the needle deep into your arm, with no regard for proper procedure")
                    time.sleep(para.Mwait)
                    print("[Health -" + str(para.largeschange) + "]")
                    player.health -= para.largeschange
                    time.sleep(para.Mwait)
                    print("Blood gushes out of your arm, which the doctor messily tries to collect in a bottle")
                    time.sleep(para.Mwait)
                    print(
                        "Using your other hand, you close your fist around the needle and yank it out, ignoring the searing pain")
                    time.sleep(para.Mwait)
                    print(
                        "You then bring it down with all your might on the doctor's arm, who releases his grip, suprised.")
                    time.sleep(para.Mwait)
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
            time.sleep(para.Mwait)
            x = para.Lwait
            for i in range(50):
                print("S̷̗̪̆͗U̷͓̚͝F̷̲̒F̷̩͕̄̕Ḙ̷̡͠R̶͖̂ ̸̹̗̂F̷̮̦͝O̷̰̎R̴̡̖̃ ̴̳̓̓Ṁ̴̹͍E̷̠͌ͅ")
                time.sleep(x)
                x /= para.Mwait
            t_end = time.time() + 1
            while time.time() < t_end:
                print("S̷̗̪̆͗U̷͓̚͝F̷̲̒F̷̩͕̄̕Ḙ̷̡͠R̶͖̂ ̸̹̗̂F̷̮̦͝O̷̰̎R̴̡̖̃ ̴̳̓̓Ṁ̴̹͍E̷̠͌ͅ")
            if skillcheck(player.luck, 50) == True:
                print("You cast  them out of your head and press on")
                time.sleep(para.Mwait)
                print("You won't let them try to control you anymore")
                time.sleep(para.Mwait)
                print("Sanity fully restored")
                Sanity = 100
            else:
                print("You shakily draw a knife and plunge it into your stomach")
                time.sleep(para.Mwait)
                print("[Health -" + str(atk) + "]")
                player.health -= atk

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

        misc.distance += 1
        if misc.distance > misc.difficulty:
            misc.difficulty = misc.distance
        player.hunger -= para.smallchange


def ending():
    if misc.distance >= 50:
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