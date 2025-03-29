from character_sheets import player
import time
import random
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
    def __init__():
        super().__init__(1, 101, "flavour")
    def text(self):
        print("gloom and paranoia fill the air")

class Nsaneflavourc(encounters):
    def __init__():
        super().__init__(1, 50, "Nsaneflavour")
    def text(self, para):
        print("insane event")


class foodfindc(encounters):
    def __init__():
        super().__init__(1, 101, "meat")
    def text(self, player):
        print("You found some meat!")
        player.inv["meat"] +=1

class pillfindc(encounters):
    def __init__():
        super().__init__(1, 101, "Nsaneflavour")
    def text(self, player):
        print("You found some pills!")
        player.inv["pills"] += 1

class bandagefindc(encounters):
    def __init__():
        super().__init__(1, 101, "bandages")
    def text(self, player):
        print("You found some bandages!")
        player.inv["bandages"] += 1

class goldfindc(encounters):
    def __init__():
        super().__init__(1, 101, "goldfind")
    def text(self, player):
        print("You found some gold!")
        player.gold += 1

class itemfindc(encounters):
    def __init__():
        super().__init__(1, 101, "itemfind")
    def text(self, player):
        print("This function doesn't currently work.")
        print("I'll get back to it later")

class slimec(encounters):
    def __init__():
        super().__init__(2, 101, "slime")
    def text(self, para player):
        print("Combat encounter: slime")

class zombiec(encounters):
    def __init__():
        super().__init__(2, 101, "zombie")
    def text(self, para, player):
        print("Combat encounter: zombie")

class shadowc(encounters):
    def __init__():
        super().__init__(2, 50, "shadow")
    def text(self, para, player):
        print("Combat encounter: shadow")

class lootcorpsec(encounters):
    def __init__():
        super().__init__(2, 101, "lootcorpse")
    def text(self, para, player):
        print("corpse looting: ignore, gain materials at cost of sanity or fight zombie ")
        print("At high diff, fight skinwalker")

class lore1c(encounters):
    def __init__():
        super().__init__(3, 101, "lore1")
    def text(self, para):
        print("lore1: paper about energy in sea")

class shrinec(encounters):
    def __init__():
        super().__init__(3, 101, "shrine")
    def text(self, player, para):
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

class konamic(encounters):
    def __init__():
        super().__init__(3, 101, "c-ritual")
    def text(self, para, player):
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

class drinkc(encounters):
    def __init__():
        super().__init__(3, 101, "drink")
    def text(self, para, player):
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
            if random.randint(0, 100) + player.luck - (player.doom/10) > 50:
                print("Cool, refreshing water flows down the tap, revitalising your body and mind")
                time.sleep(para.Mwait)
                print("[Sanity +" + str(para.v.smallchange) + "]")
                player.sanity += para.v.smallchange
                if sanity > 100:
                    sanity = 100
            else:
                print("The faucet turns on, but it doesn't produce water")
                time.sleep(para.Mwait)
                print("Instead, blood flows down, coating your hands and feet")
                time.sleep(para.Mwait)
                print("[Sanity -" + str(para.v.smallchange) + "]")
                player.sanity -= para.v.smallchange
        else:
            print("You decide to ignore it, the water isn't safe.")
            time.sleep(para.Mwait)
            print("But your thirst has become dire, and you find yourself growing weaker because of it")
            time.sleep(para.Mwait)
            print("[Health -" + str(para.smallschange) + "]")
            player.health -= para.smallschange

class deersacc(encounters):
    def __init__():
        super().__init__(4, 101, "deersac")
    def text(self, para, player):
        print("See fawn strapped to altar, can kill it to reduce doom at cost of sanity")

class batterc(encounters):
    def __init__():
        super().__init__(5, 101, "batter")
    def text(self, para, player):
        print("Combat encounter: batter")

class shopc(encounters):
    def __init__():
        super().__init__(6, 101, "shop")
    def text(self, para, player):
        print("shop")

class gnasherc(encounters):
    def __init__():
        super().__init__(7, 101, "gnasher")
    def text(self, para, player):
        print("Combat encounter: gnasher")

class sorrowc(encounters):
    def __init__():
        super().__init__(10, 101, "sorrow")
    def text(self, para, player):
        print("Combat encounter: sorrow")

class crowc(encounters):
    def __init__():
        super().__init__(13, 101, "crow")
    def text(self, para, player):
        print("Combat encounter: crow")

class tunnelchasec(encounters):
    def __init__():
        super().__init__(15, 101, "tunnelchase")
    def text(self, para, player):
        print("Combat encounter: digger")

class lore2c(encounters):
    def __init__():
        super().__init__(15, 101, "lore2")
    def text(self, para, player):
        print("Scientist research paper")

class stalkerc(encounters):
    def __init__():
        super().__init__(15, 101, "tunnelchase")
    def text(self, para, player):
        print("Combat encounter: stalker")

class beelzebubc(encounters):
    def __init__():
        super().__init__(15, 50, "beelzebub")
    def text(self, para, player):
        print("Combat encounter: glutton")

class blackcatc(encounters):
    def __init__():
        super().__init__(15, 101, "blackcat")
    def text(self, para, player):
        print("eat cat to lose sanity for hunger or pet cat for luck decrease")
        print("If sanity is low and pet cat, fight cheshire")

class restc(encounters):
    def __init__():
        super().__init__(15, 101, "rest")
    def text(self, para, player):
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
    def __init__():
        super().__init__(15, 101, "mugging")
    def text(self, para, player):
        print("Give all money or fight 3 consecutive masked men")

class mansionc(encounters):
    def __init__():
        super().__init__(15, 101, "mansion")
    def text(self, para, player):
        print("Stay at creepy guy's mansion")

class doctorc(encounters):
    def __init__():
        super().__init__(16, 101, "doctor")
    def text(self, para, player):
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
    def __init__():
        super().__init__(16, 101, "sacrifice")
    def text(self, para, player):
        print("Sacrifice health for statboost/lower doom")

class witchc(encounters):
    def __init__():
        super().__init__(16, 101, "witch")
    def text(self, para, player):
        print("Offered a potion which will restore/harm or raise/lower a stat")

class cultc(encounters):
    def __init__():
        super().__init__(17, 101, "cult")
    def text(self, para, player):
        print("Perform ritual with cult to raise doom or fight members consecutively")
        print("If doom is high, cultists get a stat increase")

class altarc(encounters):
    def __init__():
        super().__init__(17, 101, "altar")
    def text(self, para, player):
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

class crawlerc(encounters):
    def __init__():
        super().__init__(17, 101, "crawler")
    def text(self, para, player):
        print("Combat encounter: crawler")

class mirrorc(encounters):
    def __init__():
        super().__init__(20, 101, "mirror")
    def text(self, para, player):
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
            player.sanity -= para.v.smallchange

class hunterc(encounters):
    def __init__():
        super().__init__(20, 101, "hunter")
    def text(self, para, player):
        print("Combat encounter: hunter")

class mimicc(encounters):
    def __init__():
        super().__init__(17, 101, "mimic")
    def text(self, para, player):
        print("Combat encounter: mimic")

class lore3c(encounters):
    def __init__():
        super().__init__(20, 101, "lore3")
    def text(self, para):
        print("cult room")

class trapc(encounters):
    def __init__():
        super().__init__(25, 101, "trap")
    def text(self, para, player):
        print("Chance for item or take damage")

class fleshortcutc(encounters):
    def __init__():
        super().__init__(25, 101, "fleshortcut")
    def text(self, para, player):
        print("fleshortcut")

class amigarac(encounters):
    def __init__():
        super().__init__(, 101, "amigara")
    def text(self, para, player):30
        print("go through crack, gain distance but lose health, max sanity and hunger to 50 and gain attack")

class holesc(encounters):
    def __init__():
        super().__init__(30, 101, "holes")
    def text(self, para, player):
        print("Sees holes on hand, can either cut it out and take damage, or let holes spread for reduced max hp")

class saviorc(encounters):
    def __init__():
        super().__init__(30, 101, "savior")
    def text(self, para, player):
        print("Fight consecutive battles and be rewarded or ignore at sanity cost")

class almalgamc(encounters):
    def __init__():
        super().__init__(35, 101, "amalgam")
    def text(self, para, player):
        print("Combat encounter: Amalgam")

class angelc(encounters):
    def __init__():
        super().__init__(35, 50, "angel")
    def text(self, para, player):
        print("Combat encounter: Angel")

class gods_callingc(encounters):
    def __init__():
        super().__init__(35, 50, "gods_calling")
    def text(self, para, player):
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

class maskedbasec(encounters):
    def __init__():
        super().__init__(40, 101, "masked base")
    def text(self, para, player):
        print("Can either sneak by, steal food or turn back")
        print("stealing food has higher chance of failure, turning back results in loss of distance")
        print("if caught, fight 2 masked men and then leader")

class terrorc(encounters):
    def __init__():
        super().__init__(40, 50, "terror")
    def text(self, para, player):
        print("Combat encounter: Terror")

class dollc(encounters):
    def __init__():
        super().__init__(40, 101, "doll")
    def text(self, para, player):
        print("Combat encounter: doll")

class hydrac(encounters):
    def __init__():
        super().__init__(40, 101, "hydra")
    def text(self, para, player):
        print("Combat encounter: Hydra")

class skinwalkerc(encounters):
    def __init__():
        super().__init__(40, 101, "skinwalker")
    def text(self, para, player):
        print("Combat encounter: skinwalker")

class HADc(encounters):
    def __init__():
        super().__init__(40, 101, "H.A.D")
    def text(self, para, player):
        print("Combat encounter: H.A.D")

foodfind = foodfindc()
pillfind = pillfindc()
bandagefind = bandagefindc()
goldfind = goldfindc()
itemfind = itemfindc()
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
hydra = hydrac
skinwalker = skinwalkerc()
HAD = HADc()

#encounters = different events which can occur
eventable = [flavour, Nsaneflavour, foodfind, bandagefind, pillfind, goldfind, itemfind, slime, zombie, shadow, lootcorpse, lore1, shrine, konami, deersac, drink, batter, corpse, gnasher, taxes, sorrow,tunnelchase, shop, lore2, crow, stalker, beelzebub, blackcat, rest, mugging, mansion, doctor, sacrifice, cult, altar, fleshortcut, hunter, crawler, mirror, mimic, witch, lore3, trap, amigara, amalgam, angel, gods_calling, maskedbase, terror, savior, doll, hydra, skinwalker, HAD]
validevents = []

def encounterpick(allevents, validevents):
    from characer_sheets import player.sanity
    from parameters import misc.difficulty
    from parameters import para.Lwait
    for i in range(len(eventable)):
        if misc.difficulty >= eventable[i].diff and player.sanity <= eventable[i].san:
            validevents.append(eventable[i])
    event = validevents[random.randint(0, len(validevents) - 1)]
    return (event.text)