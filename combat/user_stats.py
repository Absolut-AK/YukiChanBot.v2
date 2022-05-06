class UserStats():
    def __init__(self):
        self.power = 0
        self.speed = 0
        self.agility = 0
        self.attack = 0
        self.endurance = 0

    def statCalculation(self, *args):
        for i in args:
            if 'power' in i:
                self.power += i.get('power')
            if 'attack' in i:
                self.attack += i.get('attack')
            if 'speed' in i:
                self.speed += i.get('speed')
            if 'agility' in i:
                self.agility += i.get('agility')
            if 'endurance' in i:
                self.endurance += i.get('endurance')

        return {'power':self.power, 'attack':self.attack, 'speed':self.speed, 'agility':self.agility, 'endurance':self.endurance}

s = UserStats()

boots = {"power": 10, "agility":10}
weapon = {"power":10, "attack":10, "speed":10}
pants = {"power":10, "attack":10, "speed":10}

print(s.statCalculation(boots, weapon, pants))