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
        self.hide_card = True
        self.player.player_end = False
        self.dealer.dealer_end = False
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
            self.run_dealer()

    def run_dealer(self):
        while self.dealer.dealer_end == False:
            self.dealer.total()
            self.dealer.soft17()
            self.hide_card = False
            if self.dealer.isbust == True:
                self.isresult = "Win"
                self.turn = None
                return self.isresult
            self.dealer.stand()
            if self.dealer.isstand == True:
                break
            else:
                self.dealer.hit()
                if self.dealer.isbust == True:
                    self.isresult = "Win"
                    self.turn = None
                    return self.isresult
        self.turn = None
        self.result()

    def result(self):
        if self.player.hand_total > self.dealer.hand_total and self.player.player_end == True and self.dealer.dealer_end == True:
            self.isresult = "Win"
        elif self.player.hand_total < self.dealer.hand_total and self.player.player_end == True and self.dealer.dealer_end == True:
            self.isresult = "Loss"
        elif self.player.hand_total == self.dealer.hand_total and self.player.player_end == True and self.dealer.dealer_end == True:
            self.isresult = "Push"
        return self.isresult

