from blackjack.gameplay.player import Player
from blackjack.gameplay.dealer import Dealer

class GameEngine:
    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.turn = "player"
        self.hide_card = True
        self.round = 0
        self.isresult = None

    def start_round(self):
        self.turn = "player"
        self.hide_card = True
        self.isresult = None
        self.player.isblackjack = False
        self.player.isbust = False
        self.player.player_end = False
        self.dealer.isblackjack = False
        self.dealer.isbust = False
        self.dealer.dealer_end = False
        self.player.hand = []
        self.dealer.hand = []
        self.hide_card = True
        self.player.deal()
        self.dealer.deal()
        self.player.total()
        self.dealer.total()
        self.player.blackjack()
        self.dealer.blackjack()
        self.turn = "player"
        self.player.isfirst = True
        self.round += 1
        self.isresult = None
        if self.player.isblackjack == True and self.dealer.isblackjack == True:
            self.isresult = "Push"
            self.hide_card = False
            self.turn = None
            return self.isresult
        if self.player.isblackjack == True:
            self.isresult = "Win"
            self.hide_card = False
            self.turn = None
            return self.isresult
        if self.dealer.isblackjack == True:
            self.hide_card = False
            self.isresult = "Loss"
            self.turn = None
            return self.isresult

    def player_hit(self):
        if self.turn == "player":
            self.player.hit()
        if self.player.isbust == True:
            self.isresult = "Loss"
            self.turn = None
            return self.isresult
    
    def player_double(self):
        if self.player.isfirst == True and self.turn == "player":
            self.player.double()
            self.turn = "dealer"
        if self.player.isbust == True:
            self.isresult = "Loss"
            self.turn = None
            return self.isresult

    def player_stand(self):
        if self.turn == "player":
            self.player.stand()
            self.turn = "dealer"
            self.run_dealer_step()

    def run_dealer_step(self):
        if self.turn is None or self.dealer.dealer_end:
            return
        self.hide_card = False
        self.dealer.total()
        self.dealer.soft17()
        if self.dealer.isbust:
            self.isresult = "Win"
            self.turn = None
            return
        self.dealer.stand()

        if self.dealer.isstand:
            self.dealer.dealer_end = True
            self.turn = None
            self.result()
        else:
            self.dealer.hit()
            if self.dealer.isbust:
                self.isresult = "Win"
                self.turn = None
                return
    

    def result(self):
        if self.player.hand_total > self.dealer.hand_total and self.player.player_end == True and self.dealer.dealer_end == True:
            self.isresult = "Win"
        elif self.player.hand_total < self.dealer.hand_total and self.player.player_end == True and self.dealer.dealer_end == True:
            self.isresult = "Loss"
        elif self.player.hand_total == self.dealer.hand_total and self.player.player_end == True and self.dealer.dealer_end == True:
            self.isresult = "Push"
        return self.isresult

