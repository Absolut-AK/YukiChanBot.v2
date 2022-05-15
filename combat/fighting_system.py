class Fight():
    def __init__(self, user, n1, n2, n3, n4, n5, n6):
        self.user = user
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.n5 = n5
        self.n6 = n6
        self.enemy = [n1, n2, n3, n4, n5, n6]

    def fightingSytem(self, enemyN, ability=None):
        i = self.n1.get('health')
        while self.checkHp():
            print(self.n1.get('health'))
            i -= 1
            self.n1['health'] = i
    
    def fightingLog(self):
        pass
    
    def attackChoice(self, ability, enemyN):
        print(enemyN, self.n1)
        if enemyN == '1':
            enemyN = self.n1
        elif enemyN == '2':
            enemyN = self.n2
        elif enemyN == '3':
            enemyN = self.n3
        elif enemyN == '4':
            enemyN = self.n4
        elif enemyN == '5':
            enemyN = self.n5
        elif enemyN == '6':
            enemyN = self.n6
        
        return enemyN, ability
    
    def checkHp(self):
        for i in self.enemy:
            print(i)
            if i.get('health') == None or i.get('health') > 0:
                return True
            else:
                return False