import random
from gameplay.hand import Hand

class Player(Hand):
    def __init__(self):
        super().__init__(self)
        self.first_action = False
        self.doubled = False
        self.player_end = False
        self.deal = False
        self.stand = False

    def deal(self):
        super.deal()
        self.isdeal = True
        return self.isdeal
        
    def first_action(self):
        if self.isdeal == True:
            self.first_action = True
            return self.first_action

    def split(self): #may remove if it gets to complicated
        if first_action == True:
            hand1 = self.hand[0]
            hand2 = self.hand[1]
        hand1 = super.hit(hand1)
        hand2 = super.hit(hand2)
        for hand1:
            self.total = super.total()
            self.blackjack = super.blackjack()
            return self.total_hand1, self.blackjack_hand1
        for hand2:
            self.total = super.total()
            self.blackjack = super.blackjack()
            return self.total_hand2, self.blackjack_hand2
        return self.hand1, self.hand2, self.total_hand1, self.total_hand2, self.blackjack_hand1, self.blackjack_hand2

    def double(self):
        if first_action == True:
            self.hand = super.hit(self.hand)
            self.total = super.total(self.hand)
            #add a line about the bet doubling
            self.doubled = True
            return hand, doubled
        if self.doubled == True:
            self.player_end = True
            return self.player_end

    def hit(self):
        super.hit()
        self.total = super.total()
        return self.new_card, self.hand_total, self.hand 

    def stand(self):
        self.stand = True
        if self.stand == True:
            self.player_end = True
            return self.player_end, self.stand

    def bust_check():
        self.total = super.total(self.hand)
        if self.total > 21:
            super.bust()
            return self.bust, self.hand_end




