class UserStats():
    def __init__(self):
        self.health = 0
        self.power = 0
        self.speed = 0
        self.agility = 0
        self.attack = 0
        self.endurance = 0

    def statCalculation(self, *args):
        for i in args:
            if i != None:
                if 'health' in i and i.get('health') != None:
                    self.health += i.get('health')
                if 'power' in i and i.get('power') != None:
                    self.power += i.get('power')
                if 'attack' in i and i.get('attack') != None:
                    self.attack += i.get('attack')
                if 'speed' in i and i.get('speed') != None:
                    self.speed += i.get('speed')
                if 'agility' in i and i.get('agility') != None:
                    self.agility += i.get('agility')
                if 'endurance' in i and i.get('endurance') != None:
                    self.endurance += i.get('endurance')
        return {'health':self.health, 'power':self.power, 'attack':self.attack, 'speed':self.speed, 'agility':self.agility, 'endurance':self.endurance}