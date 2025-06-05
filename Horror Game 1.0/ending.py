




import time
from character_sheets import player, leader
from parameters import para
from combat import fight
import random


def ZathKopchyla():
    print("\n\n\n\n\n\n\n\nFinally, you reach your destination")
    time.sleep(para.Mwait)
    print("The imposing tower of Vexon Industries looms over you, once a symbol of prosperity and innovation")
    time.sleep(para.Mwait)
    print("Now the only thing it evokes is evil and sickness")
    time.sleep(para.Mwait)
    print("The very building itself seems to pulsate and gasp, veins poking through the cracks of the decrepit outer walls")
    time.sleep(para.Mwait)
    print("A beacon of purple energy shoots out of the roof, birthed from the occult ritual taking place")
    time.sleep(para.Mwait)
    print("All of your hardships, everything you encountered and suffered on your quest")
    time.sleep(para.Mwait)
    print("It all started here")
    time.sleep(para.Mwait)
    print("And this is where it will end")
    time.sleep(para.Mwait)
    print("Zath-Kopchyla cannot be summoned")
    time.sleep(para.Lwait)

    def sanitycheck():
        print("As you climb the tower you feel the Elder God calling out to you")
        time.sleep(para.Mwait)
        print("This attack on your SANITY is stronger than anything you've ever felt before")
        time.sleep(para.Mwait)
        if player.sanity > 50:
            print("However, your mind still holds strong")
        else:
            print("Terror wracks your mind as you feel yourself losing control of your body")
            time.sleep(para.Mwait)
            print("With shaky hands, you raise your dagger to your throat and pierce through the skin")
            time.sleep(para.Mwait)
            print("However, some semblance of willpower left in you stops you from going deeper")
            time.sleep(para.Mwait)
            print("[Health -2]")
            player.health -= 2
            print("Your mind is a wreck, shadows race across the room, figures dance across your vision taunting you, and reality itself seems to fall apart")
            time.sleep(para.Mwait)
            print("But you can't die here\nYou've come too far for that")

    def hungercheck():
        print("As the presence of the Elder God grows stronger, so to does your HUNGER")
        time.sleep(para.Mwait)
        print("It becomes all-consuming, begging for blood to be spilled")
        time.sleep(para.Mwait)
        if player.hunger > 50:
            print("However, you manage to keep it under control, thankful that you didn't enter with an empty stomach")
        else:
            print("The ache in your chest becomes unbearable, and you find yourself unable to continue")
            time.sleep(para.Mwait)
            print("[Hunger -50]")
            player.hunger -= 50
            print("But you can't just give up here\nYou've come too far for that")
            time.sleep(para.Mwait)
            print("Grabbing your dagger, you carve out a chunk of your own flesh and stuff it down your throat")
            time.sleep(para.Mwait)
            print("You will finish this. No matter what")
            time.sleep(para.Mwait)
            print("[Health -2]")
            player.health -= 2

    def concheck():
        print("As you near the Elder God, your body is suddenly overwhelmed by immense pain!")
        time.sleep(para.Mwait)
        if player.maxhealth < 15:
            print("The pain is unbearable, like a thousand daggers digging into your flesh")
            time.sleep(para.Mwait)
            print("[Health -2]")
            time.sleep(para.Mwait)
            print("If only you had improved your HEALTH, you may have been able to resist the pain")
            player.health -= 2
        else:
            print("However pain is no stranger to you, and your journey has tempered your body and improved your HEALTH- allowing you to ignore it and press on")

    def luckcheck():
        print("Climbing the building, you find the door to the next stairway locked, with two keys placed on identical pedestals near the entrance")
        time.sleep(para.Mwait)
        print("It seems only one of them is real, though only LUCK will show which one it is.")
        if player.luck < 5:
            print("As you reach for one of the keys, rows of teeth shoot out of the pedestal, causing it to bite down onto your hands")
            time.sleep(para.Mwait)
            print("You eventually manage to get your hand free of the creature's mouth, but not without severely lacerating your hand")
            time.sleep(para.Mwait)
            print("[Health -2]")
            player.health -= 2
        else:
            print("It seems luck is on your side, as you are able to grab the right key and open the door without any effort")

    def strengthcheck():
        print("As you near the top of the building, the doorway to the next stairway suddenly becomes covered in eyes!")
        time.sleep(para.Mwait)
        print("As you step back the room distorts, causing tentacles to approach from the walls and restrain you")
        time.sleep(para.Mwait)
        print("You furiously ATTACK the tentacles as hard as you can, hoping to break free")
        time.sleep(para.Mwait)
        if player.atk < 5:
            print("However your strength fails you, and you feel the tendrils squeeze down on you- cutting off your bloodflow")
            time.sleep(para.Mwait)
            print("Just as you are about to pass out, you are released")
            time.sleep(para.Mwait)
            print("[Health -2]")
            player.health -= 2

    def goldcheck():
        print("As you climb the top of the building, you run into a familiar face bound in chains")
        time.sleep(para.Mwait)
        print("'AahH! VaLuEd CuSsStOmErR!'")
        time.sleep(para.Mwait)
        print("I'm aFrAiD yOuR mEmBeRsHiP wItH UsS HaS5 ExPirEd! I mU5t TeRmInAtE oUr pArTnErShIp HeRe")
        time.sleep(para.Mwait)
        print("It seems that the shopkeeper has double crossed you, though maybe you could still bribe her with GOLD")
        time.sleep(para.Mwait)
        if player.gold < 5:
            print("Unfortunately, you don't have enough")
            time.sleep(para.Mwait)
            print("Chains are sent hurtling through your body, tearing through the flesh like paper")
            time.sleep(para.Mwait)
            print(''"I hOpE YoU cOmE aGaIn SoOoN!'")
            time.sleep(para.Swait)
            print("The shopkeeper leaves with a cackle, abandoning you in a pool of your own blood")
            time.sleep(para.Mwait)
            print("[Health -2]")
            player.health -= 2

        else:
            print("Luckily, you have enough gold in your pocket to satisfy her, and she lets you past")

    floors = [sanitycheck, hungercheck, concheck, luckcheck, strengthcheck, goldcheck]

    print("\n[WARNING: This is the final stretch. It is highly recommended you use any items to ensure your stats are high before proceeding]")
    floor = 0
    while True:
        if player.health < 1:
            break
        print("You are on floor", floor)
        print("Health:", str(player.health) + "/" + str(player.maxhealth))
        climbing = input("Press I to access inventory\n")
        if climbing == "i":
            from invmenu import inventory
            inventory()
        elif floor >= 3:
            break
        else:
            level = floors[random.randint(0, len(floors) - 1)]
            print("\n\n\n\n\n")
            level()
            time.sleep(para.Mwait)
            print("\n\n\n\n\n")
            floor += 1

    if player.health < 1:
        print("Unfortunately, your wounds have become too much to bear")
        time.sleep(1)
        print("You were so close, and yet it was all for naught in the end")
        time.sleep(1)
        print("GAME OVER")
        player.hunger = 100
        player.sanity = 100

    else:
        print("Finally, you make it to the top of the tower")
        time.sleep(para.Mwait)
        print("A large cult stands on the roof, gathered round a large stone obelisk")
        time.sleep(para.Lwait)
        print("The obelisk is cracked in several places, and you feel an overwhelming amount of power from it")
        time.sleep(para.Lwait)
        print("Purple energy crackles all over the place, and both the sky and ground seem to be curving inwards, as if reaching towards the obelisk")
        time.sleep(para.Mwait)
        print("Reality has no jurisdiction in this place")
        time.sleep(para.Lwait)
        print("The leader of the cult notices you and cackles to himself")
        time.sleep(para.Lwait)
        print("'Have you come to stop us? Well you're too late!'")
        time.sleep(para.Lwait)
        print("'There is no use trying to defy the Old One's will, it is inevitable!'")
        time.sleep(para.Lwait)
        print("'Now, let me demonstrate to you the power bestowed upon to me by Zath-Kopchyla!'")
        if fight(leader):
            time.sleep(para.Mwait)
            print("Bloodied and beaten, the cult leader scowls at you")
            time.sleep(para.Mwait)
            print("'Why do you still fight? It is pointless!'")
            time.sleep(para.Lwait)
            print("'You may have defeated me, but the end result is the same'")
            time.sleep(para.Lwait)
            print("'For an Elder God such as her cannot be stopped!'")
            time.sleep(para.Lwait)
            print("The cult leader stands up")
            time.sleep(para.Mwait)
            print("'Now, rise Zath-Kopchyla! Oh Great One! Oh Mother of the Abyss!'")
            time.sleep(para.Lwait)
            print("'From the pitch black bosom of darkness we came, and there we shall return!'")
            time.sleep(para.Lwait)
            print("'For you are all that is eternal! The loving embrace of darkness shall always be present, for all of time!'")
            time.sleep(para.Lwait)
            print("'Now! Accept this sacrifice Zath-Kopchyla! So that you may grace us with your presence and return this world to darkness once more!'")
            time.sleep(para.Lwait)
            print("With that, the lead cultist raises his dagger and plunges it into his chest. The rest of the cult soon follow in his lead")
            time.sleep(para.Lwait)
            print("In response to the cult's sacrifice, the cracks in the obelisk grow even wider")
            time.sleep(para.Lwait)
            print("To your horror, you see something beginning to poke it's way out of the obelisk")
            time.sleep(para.Lwait)
            print("Taking action, you rush towards the obelisk, and begin to push it towards the edge of the roof")
            time.sleep(para.Mwait)
            print("Tentacles begin to pour out of it, stabbing at your hands, as deafening shouts ring throughout your ears")
            time.sleep(para.Lwait)
            print("Each step you take feels extremely slow and heavy, as if the creature is distorting gravity to stop you")
            time.sleep(para.Lwait)
            print("The ground digs into your body, trying to trap your feet, and the obelisk begins to heat up to smoldering temperatures")
            time.sleep(para.Lwait)
            print("But even as your feet become mangled beyond repair, even when the flesh starts melting off of your hands, you keep going until you reach the edge of the building")
            time.sleep(para.Lwait)
            print("With your arms fully melted off, you divert the last of your strength into pushing yourself against the obelisk as hard as possible")
            time.sleep(para.Lwait)
            print("At last, the obelisk tips and is sent plummeting down the side of the building, alongside your unconscious body")
            time.sleep(para.Lwait)
            print("As both flesh and stone meet the ground, they are destroyed beyond recognition, releasing a burst of energy which engulfs the entire city")
            time.sleep(para.Lwait)
            print("The portal has been closed and without any connection to the source, any traces of Zath-Kopchyla's influence disappear as well")
            time.sleep(para.Lwait)
            print("At last, you were able to defeat the cult and stop the Elder God from being summoned, even if it cost you for life")
            time.sleep(para.Lwait)
            print("But the world will rest easy knowing that Zath-Kopchyla will haunt them no more")
            time.sleep(para.Lwait)
            print("At least, for now...")
            time.sleep(para.Lwait)
            player.hunger = 100
            player.sanity = 100

        else:
            print("Was it truly all for nothing?")
            time.sleep(para.Lwait)
            print("As you are held up to be sacrificed, you can't help but think about what could have been")
            time.sleep(para.Mwait)
            print("If only you were stronger")
            time.sleep(para.Swait)
            print("If only you hadn't missed that attack")
            time.sleep(para.Swait)
            print("If only you had prepared more")
            time.sleep(para.Swait)
            print("But it's too late now")
            time.sleep(para.Mwait)
            print("You were so close to saving everyone, so close to making it all a distant nightmare")
            time.sleep(para.Mwait)
            print("And yet, you failed")
            time.sleep(para.Mwait)
            print("But then again, maybe you never had a chance in the first place")
            time.sleep(para.Mwait)
            print("You were a fool to think you could ever stop something as powerful as a God")
            time.sleep(para.Mwait)
            print("As the knife falls and punctures through your heart, you have no-one to blame but yourself")
            time.sleep(para.Mwait)
            print("[GAME OVER]")
            player.hunger = 100
            player.sanity = 100