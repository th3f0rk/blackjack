import random
from blackjack.gameplay.hand import Hand

class Dealer(Hand):
    def __init__(self):
        super().__init__()
        self.issoft17 = False
        self.isstand = False
        self.dealer_end = False

    def deal(self):
       super().deal()
       self.isbust = False
       self.issoft17 = False
       self.isstand = False
       self.dealer_end = False
       return self.hand

    def soft17(self):
        self.hand_total = super().total()
        self.issoft17 = False
        if self.hand_total == 17:
            for rank, value in self.hand:
                if value == 11:
                    self.issoft17 = True
                    break
        return self.issoft17
    
    def stand(self):
        self.hand_total = super().total()
        if self.hand_total >= 17 and self.issoft17 == False:
            self.isstand = True
            self.dealer_end = True
            return self.dealer_end

    def hit(self):
        self.hand_total = super().total()
        if self.hand_total <17 or self.issoft17 == True:
            self.hand = super().hit()
        super().total()
        self.bust()
        return self.hand

    def bust(self):
        super().bust()
        if self.isbust == True:
            self.dealer_end = True
        return self.dealer_end

