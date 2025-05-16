class misc:
    def __init__(self, hasgun, stalking, distance, difficulty):
        self.hasgun = hasgun
        self.stalking = stalking
        self.distance = distance
        self.difficulty = difficulty
#hasgun = Determines whether to add ammo to the itempool
#stalking = Determines whether the player is being stalked
#distance = The players current distance and difficulty

misc = misc(False, -1, 1, 1)


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


para = paracelsus(1, 1.5, 2, 10, 20, 1, 2, 30, 50, 3, 5)





# class inventory:
#     def __init__(self, food, bandage, pills, knives, acid, rbtfoot, roids, ammo, charm, effigy):
#         self.food = food
#         self.bandage = bandage
#         self.pills = pills
#         self.knives = knives
#         self.acid = acid
#         self.rbtfoot = rbtfoot
#         self.roids = roids
#         self.ammo = ammo
#         self.charm = charm
#         self.effigy = effigy
#Items get appended to the list when added to inventory, duplicates increase the value of the corresponding variable

#inv = inventory(5, 0, 0, 0, 0, 0, 0, 0, 0, 0)
#items = ["meat"]


