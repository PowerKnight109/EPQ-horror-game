class misc:
    def __init__(self, hasgun, stalking, distance, difficulty):
        self.hasgun = hasgun
        self.stalking = stalking
        self.distance = distance
        self.difficulty = difficulty

#hasgun = Determines whether to add ammo to the itempool
#stalking = Determines whether the player is being stalked
#distance = The players current distance and difficulty

misc = misc(False, False, 1, 1)




class paracelsus:
    def __init__(self, Swait, Mwait, Lwait, smallchange, largechange, smallschange, largeschange, smallrestore, largerestore, smallhprestore, largehprestore):
        self.Swait = Swait
        self.Mwait = Mwait
        self.Lwait = Lwait
        self.smallchange = smallchange
        self.largechange = largechange
        self.smallschange = smallschange
        self.largeschange = largeschange
        self.smallrestore = smallrestore
        self.largerestore = largerestore
        self.smallhprestore = smallhprestore
        self.largehprestore = largehprestore
#S/M/Lwait = How long the time.sleep function should run for (Short, Medium, Large)
#small/largechange = How much values such as hunger and stamina should be changed by
#small/largeschange = How much values such as hp and gold should be changed by
#small/largerestore = How much sanity or hunger restoring items should restore
#small/largehprestore = How much health restoring items should restore

#
para = paracelsus(1, 1.5, 2, 10, 20, 1, 2, 30, 50, 3, 5)


import time
from character_sheets import player

def stalkt1():
    print("\n\n\nYou feel like you're being watched")
    time.sleep(para.Swait)
    print("[Sanity -10]")
    player.sanity -= 10

def stalkt2():
    print("\n\n\nYou hear footsteps behind you")
    time.sleep(para.Swait)
    print("[Sanity -10]")
    player.sanity -= 10

def stalkt3():
    print("\n\n\nYou spot a figure watching you from the shadows")
    time.sleep(para.Swait)
    print("[Sanity -10]")
    player.sanity -= 10

def stalkt4():
    print("\n\n\nThe figure in the shadows seems to be getting closer and closer")
    time.sleep(para.Swait)
    print("[Sanity -10]")
    player.sanity -= 10

stalktext = [stalkt1, stalkt2, stalkt3, stalkt4]



class stalkc:
    def __init__(self, switch, counter, text):
        self.switch = switch
        self.counter = counter
        self.text = text

stalking = stalkc(False, 0, stalktext)