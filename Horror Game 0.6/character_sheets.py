class stats:
    def __init__(self, name, maxhealth, health, hunger, sanity, doom, atk, luck, speed, accuracy, xp, gold, hitext, wintext, losetext, checkdesc ):
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
        self.speed = speed
        self.hitext = hitext
        self.wintext = wintext
        self.losetext = losetext
        self.checkdesc = checkdesc
        self.name = name



class protag(stats):
    def __init__(self, inv):
        self.inv = inv
        super().__init__("You", 10, 10, 100, 100, 0, 1, 0, 50, 80, 0, 0, "You attack!", "You won!", "You lost!", "It's you")


#player = protag(playername,10, 10, 100, 100, 0, 1, 0, 50, 80, 0, 0, "You attack!", "You won!", "You lost!", "It's you")
player = protag({
                    "meat": 0,
                    "pills": 0,
                    "bandages": 0,
                    "effigy": 0,
                    "charm": 0,
                    "steroids": 0,
                    "rabbitfoot": 0,
                    "acid": 0,
                    "bullets": 0,
                    "gun": False

                })

#def shadowd():
    # print("The shadowy creature dissipates into nothingness")
    # shadow.health = shadow.maxhealth

#def zombied():
#



shadow = stats("???", 3, 3,0, 50, 80, 1, 1, 60, 80, 10, 0, "The creature lunges towards you!", "The creature laughs", "The shadowy creature dissipates into nothingness", "The figure standing in front of me is not real\nThe figure standing in front of me is not real\nThe figure standing in front of me is not real")
zombie = stats("Zombie", 2, 2, 1, 100, 0, 1, 0, 1, 70, 5, 1, "The zombie flails its arms at you!", "The zombie bites down on you", "The zombie collapses", "The result of a failed ritual to harness Zath-Kopchyla's essence\n The host's soul was too weak to handle even a fraction of its power and shattered, leaving only a pathetic shambling husk behind")
slime = stats("Slime", 3, 3, 1, 100, 0, 1, 0, 5, 90, 10, 0, "The slime bites down on you!", "The slime assimilates you", "The slime melts into a puddle", "The result of a failed ritual to harness Zath-Kopchyla's power\nThe host's body was too weak to handle even a fraction of the god's essence and broke down, leaving the soul to possess the melted pile of black sludge that remained")
batter = stats("Masked Man", 5, 5, 1, 100, 0, 1, 1, 50, 80, 20, 5, "The masked man swings his bat at you!", "You are beaten to death", "The masked man collapses, defeated", "The influence of Zath-Kopchyla has infected people's minds, making them extremely aggressive\nGangs of people have begun wearing masks, patrolling the streets with baseball bats in search of any potential victims to hunt.")
gnasher = stats("Gnasher", 5, 5, 1, 100, 0, 4, 0, 100, 45, 20, 3, "The gnasher charges at you, snapping wildly!","The creature sinks it's fangs into your throat", "The gnasher slows to a halt", "A person mutated beyond recognition by Zath-Kopchyla's influence.\nThese creatures are blind, and will recklessly charge at the slightest noise they hear.\nWhile inaccurate, their attacks can pack a fatal punch.")
#enemies = [shadow, zombie, slime, batter, tax, sorrow, gnasher, stalker, digger, crow, mimic, beelzebub, hunter, crawler, amalgam, cultist, angel, hydra, skinwalker, masked_leader, doll, terror, H.A.D]

