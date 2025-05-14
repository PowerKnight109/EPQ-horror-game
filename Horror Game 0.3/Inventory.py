class encounters:
    def __init__(self, diff, san, name):
        self.diff = diff
        self.san = san
        self.name = name
        # diff = difficulty (number of steps until event can be included)
        # san = sanity (Maximum sanity value event can occur at)
        # fight = Whether event is a combat encounter or not (will be used when an event outcome leads to random fight)
        # name = name of encounter

#event\nB: adjust values\nC: speed up\n").lower()
#             if x == "a":
#                 for i in range(len(eventable)):
#                     print(eventable[i].name)
#                 print("Which event would you like to try?")
#                 event = input()
#                 if eventable[i].name == event:
#                     return  eventable[i]
#
#                 devmode = True
#             elif x == "b":
#                 y = input("What value would you like to adjust?\n")
#                 if y == "distance":
#                     z = int(input("What is the new distance?\n"))
#                     misc.distance = z
#                     continue
#             elif x == "c":
#                 print("SPEED UP!\nSPEED UP!\nSPEED UP!")
#                 para.Swait = 0
#                 para.Mwait = 0.5
#                 para.Lwait = 1
#                 continue
#
#         elif progress == "A" and len(items) < 1:
#             #prints gold amount and tells the player they have no items, then returns to start of loop
#             print("You have", player.gold, "gold")
#             time.sleep(para.Mwait)
#             print("You have no items")
#             time.sleep(para.Mwait)
#             continue
#         elif progress == "A" and len(items) >= 1:
#             print("You have", player.gold, "gold")
#             time.sleep(para.Mwait)
#             for i in range(len(items)):
#                 #prints a letter for each item in inventory eg: A,B,C,D,etc
#                 print((chr(i + 65)) + ":", items[i])
#             print(chr(len(items) + 65) + ":", "back")
#             itemuse = input("")
#             #turns letter input into a number, checks if number is in list
#             if ord(itemuse.upper()) - 65 < len(items):
#                 x = items[ord(itemuse.upper()) - 65]
#                 if x == "meat":
#                     print("meat (consumable)")
#                     time.sleep(para.Mwait)
#                     print("Restores", para.largerestore, "hunger")
#                     print("Don't ask where it's from")
#                     time.sleep(para.Mwait)
#                     print("You have:", inv.food)
#                     print("Consume the meat?")
#                     time.sleep(para.Mwait)
#                     print("A: Yes")
#                     print("B: No")
#                     y = input()
#                     if y.lower() == "a":
#                         print("You ate the meat")
#                         player.hunger += para.largerestore
#                         if player.hunger > 100:
#                             player.hunger = 100
#                         inv.food -= 1
#                         if inv.food == 0:
#                             items.remove("meat")
#             continue







from character_sheets import player


def inventory():
    words = ["meat", "pills", "bandages", "effigy", "charm", "roids", "rbtfoot", "acid", "bullets", "gun"]
    hasitems = False
    for i in range(len(words)):
        if player.inv[words[i]] > 0:
            print(words[i]+":", player.inv[words[i]])
            hasitems = True


    if hasitems == False:
        print("You have no items")

    else:
        from parameters import para
        import time

        def food():
            print("meat")
            time.sleep(para.Swait)
            print("restores", para.largerestore, "hunger\nDon't ask where it's from")
            time.sleep(para.Mwait)
            print("Consume the meat?")
            print("A: Yes\nB: No")
            y = input()
            if y.lower() == "a":
                print("You ate the meat")
                time.sleep(para.Swait)
                a = player.hunger
                player.hunger += para.largerestore
                if player.hunger > 100:
                     player.hunger = 100
                print("[Hunger restored by", str(player.hunger-a)+"]")
                player.inv["meat"] -= 1

        def pill():
            print("pills")
            time.sleep(para.Swait)
            print("restores", para.largerestore, "sanity\n Failure to take on time may lead to withdrawal")
            time.sleep(para.Mwait)
            print("Take the pills?")
            print("A: Yes\nB: No")
            y = input()
            if y.lower() == "a":
                print("You took the pills")
                time.sleep(para.Swait)
                a = player.sanity
                player.sanity += para.largerestore
                if player.sanity > 100:
                    player.sanity = 100
                print("[Sanity restored by", str(player.sanity-a)+"]")
                player.inv["pills"]-=1


        def bandage():
            print("bandages")
            time.sleep(para.Swait)
            print("restores", para.largehprestore, "health\n Don't question the logic of it")
            time.sleep(para.Mwait)
            print("Use the bandages?")
            print("A: Yes\nB: No")
            y = input()
            if y.lower() == "a":
                print("You applied the bandages")
                time.sleep(para.Swait)
                a = player.health
                player.health += para.largehprestore
                if player.health > player.maxhealth:
                    player.health = player.maxhealth
                print("[Health restored by", str(player.health-a)+"]")
                player.inv["bandages"] -= 1

        selectlist = [food, pill, bandage]
        print("Please type the name of the item you would like to view")
        itemselect = input().lower()

        if player.inv[itemselect] <= 0:
            print("You shouldn't be here")

        selectlist[words.index(itemselect)]()
        #matches the position of the item in the words list with the position of the corresponding function and runs it



inventory()