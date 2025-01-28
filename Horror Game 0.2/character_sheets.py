class stats:
    def __init__(self, maxhealth, health, hunger, sanity, doom, atk, luck, accuracy, xp, gold):
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

player = stats(10, 10, 100, 100, 0, 1, 0, 80, 0, 0)
maxhealth = player.maxhealth
health = player.health
hunger = player.hunger
sanity = player.sanity
doom = player.doom
atk = player.atk
luck = player.luck
accuracy = player.accuracy
xp = player.xp
gold = player.gold