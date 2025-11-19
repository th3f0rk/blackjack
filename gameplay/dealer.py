import random
from gameplay.hand import Hand

class Dealer(Hand):
    def __init__(self):
        super().__init__()
        self.issoft17 = False
        self.isstand = False
        self.dealer_end = False

    def deal(self):
       super.deal()
       self.isbust = False
       self.issoft17 = False
       self.isstand = False
       self.dealer_end = False
       return self.hand

    def soft17(self):
        self.hand_total = super.total()
        self.issoft17 = False
        for card in self.hand:
            if card == 11 and self.hand_total == 17:
                self.issoft17 = True
        return self.issoft17
    
    def stand(self):
        self.hand_total = super.total()
        if self.hand_total >= 17 and self.issoft17 == False:
            self.isstand = True
            self.dealer_end = True
            return self.dealer_end

    def hit(self):
        self.hand_total = super.total()
        if self.hand_total <17 or self.issoft17 == True:
            self.hand = super.hit()
        self.total()
        return self.hand

    def bust(self):
        super.bust()
        if self.isbust == True:
            self.dealer_end = True
        return self.dealer_end

