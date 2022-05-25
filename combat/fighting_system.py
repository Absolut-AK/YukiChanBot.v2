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
        self.enemy = [self.n1, self.n2, self.n3, self.n4, self.n5, self.n6]

    def fightingSytem(self, enemyN, attack):
        enemyN -= 1
        eS = self.enemy[enemyN].get('speed')
        uS = self.user.get('speed')
        if attack == 1:
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
        return self.enemy[enemyN].get('health'), self.user.get('health')

    
    def fightingLog(self):
        text = f"Your Health: {self.user.get('health')}❤ \n"
        for j, i in enumerate(self.enemy):
            if i.get('health') == None:
                pass
            elif i == self.n3 or i == self.n6 and i != None:
                text += f"Enemy{j+1}: {i.get('health')}❤ \n"
            else:
                text += f"Enemy{j+1}: {i.get('health')}❤ \t"

        return text
    
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