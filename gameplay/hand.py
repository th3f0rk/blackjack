import Random

class Hand():
    def __init__(self):
        self.hand = []
        self.bust = False
        self.blackjack = False
        self.hand_end = False

    def deal():
        card1 = random.randint(2,11)
        card2 = random.randint(2,11)
        self.hand = [card1, card2]

    def hit():
        new_card = self.hand.append(random.randint(2,11))
    
    def ace(self.hand, hand_total):
        if hand_total > 21:
            for card in self.hand:
                if card == 11:
                    self.hand.remove(card)
                    self.hand.append(1)
                else:
                    pass
            return self.hand

    def total():
        hand_total = sum(self.hand)
        self.hand = ace(self.hand)

    def blackjack(hand_total):
        if hand_total == 21:
            self.blackjack = True
            return

    def bust(hand_total):
        if hand_total > 21:
            self.bust = True
            return

    def end():
        if self.blackjack == True or self.bust == True:
            self.hand_end = True
            return



