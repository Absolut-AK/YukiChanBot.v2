class Abilities():
    def __init__(self):
        pass
    
    def checkAbility(self, dic, ability):
        if dic.get(ability) != None:
            return True
        else:
            return False