import random

class Hand:
    def __init__(self):
        self.hand = []          # list of (rank, value) tuples
        self.isbust = False
        self.isblackjack = False
        self.hand_total = 0

    def make_card(self, value):
        """Return a (rank, value) pair for a given numeric value."""
        if value == 11:
            return ('A', 11)
        if value == 10:
            # randomly choose one of the 10-value faces
            return (random.choice(['K', 'Q', 'J', 'ten']), 10)
        if value == 9:
            return ('nine', 9)
        if value == 8:
            return ('eight', 8)
        if value == 7:
            return ('seven', 7)
        if value == 6:
            return ('six', 6)
        if value == 5:
            return ('five', 5)
        if value == 4:
            return ('four', 4)
        if value == 3:
            return ('three', 3)
        if value == 2:
            return ('two', 2)

    def deal(self):
        # draw two random numeric values
        self.value1 = random.randint(2, 11)
        self.value2 = random.randint(2, 11)

        # convert them to (rank, value) cards
        self.card1 = self.make_card(self.value1)
        self.card2 = self.make_card(self.value2)

        self.hand = [self.card1, self.card2]
        return self.hand

    def hit(self):
        new_value = random.randint(2, 11)
        new_card = self.make_card(new_value)
        self.hand.append(new_card)
        return self.hand

    def total(self):
        # extract just the numeric values from (rank, value)
        values = [value for (rank, value) in self.hand]
        total = sum(values)

        # count how many Aces we have (value == 11)
        num_aces = sum(1 for (rank, value) in self.hand if value == 11)

        # demote Aces from 11 -> 1 as needed to avoid bust
        while total > 21 and num_aces > 0:
            total -= 10   # effectively turning one Ace from 11 to 1
            num_aces -= 1

        self.hand_total = total
        return self.hand_total

    def blackjack(self):
        self.hand_total = self.total()
        if self.hand_total == 21:
            self.isblackjack = True
            return self.isblackjack

    def bust(self):
        self.hand_total = self.total()
        if self.hand_total > 21:
            self.isbust = True
            return self.isbust

