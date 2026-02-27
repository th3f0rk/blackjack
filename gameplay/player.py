import random
from blackjack.gameplay.hand import Hand

class Player(Hand):
    def __init__(self):
        super().__init__()
        self.isfirst = False
        self.isdoubled = False
        self.player_end = False
        self.isstand = False

    def deal(self):
        super().deal()
        super().total()
        super().blackjack()
        self.player_end = False
        self.isbust = False
        self.isdoubled = False
        self.isstand = False
        self.isfirst = True
        return self.hand

    def double(self):
        if self.isfirst == True:
            super().hit()
            super().total()
            super().bust()
            #add a line about the bet doubling
            self.isfirst = False
            self.isdoubled = True
            self.player_end = True
            return self.hand

    def hit(self):
        super().hit()
        super().total()
        super().bust()
        if self.isfirst == True:
            self.isfirst = False
        else:
            self.isfirst = False
        if self.isbust == True:
            self.player_end = True
        return self.hand 

    def stand(self):
        self.isstand = True
        if self.isstand == True:
            self.player_end = True
            return self.player_end

