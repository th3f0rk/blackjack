import random

class Hand():
    def __init__(self):
        self.hand = []
        self.isbust = False
        self.isblackjack = False
        self.hand_total = 0

    def deal(self):
        self.card1 = random.randint(2,11)
        self.card2 = random.randint(2,11)
        self.hand = [self.card1, self.card2]
        return self.hand

    def hit(self):
        self.new_card = random.randint(2,11)
        self.hand.append(self.new_card)
        return self.hand
    
    def total(self):
        self.hand_total = sum(self.hand)
        if self.hand_total > 21:
            for card in self.hand:
                if card == 11:
                    loc = self.hand.index(card)
                    self.hand[loc] = 1
                    self.hand_total = sum(self.hand)
                    if self.hand_total <= 21:
                        break
            return self.hand_total
        return self.hand_total

    def blackjack(self):
        self.hand_total = self.total()
        if self.hand_total == 21:
            self.isblackjack = True
            return self.isblackjack

    def bust(self):
        self.hand_total = self.total()
        if self.hand_total > 21:
            self.isbust = True
            return self.isbust


