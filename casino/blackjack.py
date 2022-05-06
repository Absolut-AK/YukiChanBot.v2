import random

class BlackJack:
    def __init__(self):
        self.card = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10,
        "Jack", "Jack", "Jack", "Jack", "Queen", "Queen", "Queen", "Queen", "King", "King", "King", "King", "Ace", "Ace", "Ace", "Ace"]
        self.dealerHand = []
        self.userHand = []
    
    #starting hand
    def hand(self):
        #user starting hand
        card = random.choice(self.card)
        self.userHand.append(card)
        self.card.remove(card)
        card = random.choice(self.card)
        self.userHand.append(card)
        self.card.remove(card)

        #dealer starting hand
        card = random.choice(self.card)
        self.dealerHand.append(card)
        self.card.remove(card)
        card = random.choice(self.card)
        self.dealerHand.append(card)
        self.card.remove(card)

        return (f"Dealer has x and {self.dealerHand[1]}, you got {self.userHand[0]} and {self.userHand[1]}")

    #hit
    def hit(self):
        card = random.choice(self.card)
        self.userHand.append(card)
        self.card.remove(card)
        return card

    #stand
    def stand(self):
        userSum = self.cal(self.userHand)
        dealerSum = self.cal(self.dealerHand)

        while userSum > dealerSum and dealerSum < 17 and dealerSum < 21:
            card = random.choice(self.card)
            self.dealerHand.append(card)
            self.card.remove(card)
            dealerSum = self.cal(self.dealerHand)
    
        if dealerSum > 21:
            return "Dealer Bust"
        elif dealerSum >= 17:
            if userSum > dealerSum:
                return "You won"
            elif userSum < dealerSum:
                return "Dealer Won"
            else:
                return  "tie"
        elif dealerSum == userSum:
            return "Tie"

    #win calculations of hand and with ace
    def cal(self, hand):
        sum = 0
        aces = 0
        #calculate the sum
        for i in hand:
            if isinstance(i, int):
                sum += i
            elif i == "Jack" or i == "Queen" or i == "King":
                sum += 10
            else:
                sum += 11
        #count aces'
        if sum > 21:
            for i in hand:
                if i == 'Ace':
                    aces += 1
            while sum > 21 and aces > 0:
                aces -= 1
                sum -= 10
        return sum
