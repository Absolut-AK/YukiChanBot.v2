import random
class Slot():
    def __init__(self):
        pass 

    def percentages(self, runs):
        win = 0
        lose = 0
        while runs > 0:
            i = 0
            one = 0
            two = 0
            three = 0
            while i < 3:
                result = random.randint(1, 100)
                match result:
                    case n if n <= 5:
                        one += 1
                    case n if n <= 40 and n > 5:
                        two += 1
                    case n if n <= 100 and n > 40:
                        three += 1
                i += 1
            if one == 3 or two == 3 or three == 3:
                win += 1
            else:
                lose += 1
            runs -= 1
        print(f"wins: {win}\nLoses: {lose}")
s = Slot()
s.percentages(10)