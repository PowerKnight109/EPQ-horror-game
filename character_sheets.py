class playerstats:
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

player = playerstats("You", 10, 10, 100, 100, 0, 1, 0, 50, 80, 0, 0, "You attack!", "You won!", "You lost!", "It's you")
maxhealth = player.maxhealth
health = player.health
hunger = player.hunger
sanity = player.sanity
doom = player.doom
atk = player.atk
luck = player.luck
speed = player.speed
accuracy = player.accuracy
xp = player.xp
gold = player.gold

shadow = stats("???", 3, 3,0, 50, 80, 1, 0, 60, 80, 10, 0, "The creature lunges towards you!", "The creature laughs", "The shadowy creature disspates into nothingness", "The figure standing in front of me is not real\nThe figure standing in front of me is not real\nThe figure standing in front of me is not real")
zombie = stats("Zombie", 1, 1, 1, 100, 0, 1, 0, 1, 60, 5, 1, "The zombie flails it's arms at you!", "The zombie bites down on you", "The zombie crumbles to dust", "The result of a failed ritual to harness Zath-Kopchyla's essence\n The host's soul was too weak to handle even a fraction of its power and shattered, leaving only a pathetic shambling husk behind")
slime = stats("Slime", 3, 3, 1, 100, 0, 1, 0, 5, 70, 10, 0, "The slime bites down on you!", "The slime assimilates you", "The slime melts into a puddle", "The result of a failed ritual to harness Zath-Kopchyla's power\nThe host's body was too weak to handle even a fraction of the god's essence and broke down, leaving the soul to possess the melted pile of black sludge that remained")
batter = stats("Masked Man", 5, 5, 1, 100, 0, 1, 0, 50, 80, 20, 5, "The masked man swings his bat at you!", "You are beaten to death", "The masked man collapses, defeated", "The influence of Zath-Kopchyla has infected people's minds, making them extremely aggressive\nGangs of people have begun wearing masks, patrolling the streets with baseball bats in search of any potential victims to hunt.")

#enemies = [shadow, zombie, slime, batter, tax, sorrow, gnasher, stalker, digger, crow, mimic, beelzebub, hunter, crawler, amalgam, cultist, angel, hydra, skinwalker, masked_leader, doll, terror, H.A.D]