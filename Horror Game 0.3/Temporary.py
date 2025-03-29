# Removes an item from the inventory if it's value is 0
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





print("Press A to look at items")
        progress = input("")
        if progress == "^^vv<><>BAstart":
            x = input("DEBUG MODE ACTIVATED\nA: custom event\nB: adjust values\nC: speed up\n").lower()
            if x == "a":
                for i in range(len(eventable)):
                    print(eventable[i].name)
                print("Which event would you like to try?")
                event = input()
                if eventable[i].name == event:
                    return  eventable[i]

                devmode = True
            elif x == "b":
                y = input("What value would you like to adjust?\n")
                if y == "distance":
                    z = int(input("What is the new distance?\n"))
                    misc.distance = z
                    continue
            elif x == "c":
                print("SPEED UP!\nSPEED UP!\nSPEED UP!")
                para.Swait = 0
                para.Mwait = 0.5
                para.Lwait = 1
                continue

        elif progress == "A" and len(items) < 1:
            #prints gold amount and tells the player they have no items, then returns to start of loop
            print("You have", player.gold, "gold")
            time.sleep(para.Mwait)
            print("You have no items")
            time.sleep(para.Mwait)
            continue
        elif progress == "A" and len(items) >= 1:
            print("You have", player.gold, "gold")
            time.sleep(para.Mwait)
            for i in range(len(items)):
                #prints a letter for each item in inventory eg: A,B,C,D,etc
                print((chr(i + 65)) + ":", items[i])
            print(chr(len(items) + 65) + ":", "back")
            itemuse = input("")
            #turns letter input into a number, checks if number is in list
            if ord(itemuse.upper()) - 65 < len(items):
                x = items[ord(itemuse.upper()) - 65]
                if x == "meat":
                    print("meat (consumable)")
                    time.sleep(para.Mwait)
                    print("Restores", para.largerestore, "hunger")
                    print("Don't ask where it's from")
                    time.sleep(para.Mwait)
                    print("You have:", inv.food)
                    print("Consume the meat?")
                    time.sleep(para.Mwait)
                    print("A: Yes")
                    print("B: No")
                    y = input()
                    if y.lower() == "a":
                        print("You ate the meat")
                        player.hunger += para.largerestore
                        if player.hunger > 100:
                            player.hunger = 100
                        inv.food -= 1
                        if inv.food == 0:
                            items.remove("meat")
            continue