import random
from gameplay.hand import Hand

class Player(Hand):
    def __init__(self):
        self.hand = []
        first_action = False
        doubled = False
        player_end = False

    def first_action():
        if self.hand.len() == 2:
            first_action = True
            return first_action

    def split():
        if first_action == True:
            hand1 = self.hand[0]
            hand2 = self.hand[1]
            return hand1, hand2
        hand1 = super.hit(hand1)
        hand2 = super.hit(hand2)

    def double():
        if first_action == True:
            hand = super.hit(hand)
            #add a line about the bet doubling
            doubled = True
            return hand, doubled
        if doubled == True:
            player_end = True
            return player_end


