from abilities import Abilities

a = Abilities()

class Fight():
    def __init__(self):
        self.enemy = {"power":10, "attack":10, "speed":10, "agility":0, "critchance":0, "critdamage":0}

    def fightSetup(self):
        print(self.enemy)

f = Fight()

f.fightSetup()