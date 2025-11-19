import random
from gameplay.hand import Hand

class Dealer(Hand):
    def __init__(self):
        super().__init__(self)
        self.soft17 = False
        self.stand = False

    def deal(self):
       super.deal()
       if self.deal == True:
           return self.blackjack, self.hand, self.total, self.deal

    def soft17(self):
        self.total = super.total()
        for card in self.hand:
            if self.card == 11 and self.total == 17:
                self.soft17 = True
    
    def stand(self):
        self.total = super.total()
        if self.total >= 17 and self.soft17 == False:
            self.stand = True
            return self.stand

    def hit(self):
        self.total = super.total()
        if self.total <17 or self.soft17 == True:
            self.hand = super.hit(self.hand)

    def bust(self):
        self.total = super.total()
        if self.total > 21:
            self.bust = True
