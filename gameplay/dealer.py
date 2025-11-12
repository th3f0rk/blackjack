import random
from gameplay.hand import Hand

class Dealer(Hand):
    def __init__(self):
        self.hand = []
        soft17 = False
        stand = False
        bust = False


    def soft17():
        total = super.total(self.hand)
        for card in self.hand:
            if card == 11 and total == 17:
                soft17 = True
    
    def stand():
        total = super.total(self.hand)
        if total >= 17 and soft17 == False:
            stand = True
            return stand

    def hit():
        total = super.total(self.hand)
        if total <17 or soft17 == True:
            hand = super.hit(self.hand)

    def bust():
        total = super.total(self.hand)
        if total > 21:
            bust = True
