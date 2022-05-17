import re


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
        eS = self.enemy[enemyN].get('speed')
        uS = self.user.get('speed')
        if ability == None or 'a':
            #attack
            if eS >= uS:
                if self.enemyAttack(enemyN):
                    self.userAttack(enemyN)
            else:
                if self.userAttack(enemyN):
                    self.enemyAttack(enemyN)
        else:
            #ability
            pass
        print(self.n1.get('health'), self.user.get('health'))

    
    def fightingLog(self):
        pass
    
    def userAttack(self, enemyN):
        print('uAttack')
        eH = self.enemy[enemyN].get('health')
        uA = self.user.get('attack')
        
        result = eH - uA
        self.enemy[enemyN]['health'] = result
        
        if result > 0:
            return True
        else:
            return False

    def enemyAttack(self, enemyN):
        print('eAttack')
        uH = self.user.get('health')
        eA = self.enemy[enemyN].get('attack')
        result = uH - eA
        self.user['health'] = result

        if result > 0:
            return True
        else:
            return False

    def checkHp(self):
        for i in self.enemy:
            if i.get('health') == None or i.get('health') > 0:
                return True
            else:
                return False