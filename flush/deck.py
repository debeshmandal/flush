import numpy as np

class Card():
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

class CardContainer:
    def __init__(self, cards):
        pass

    @property
    def N(self):
        return len(self.cards)

    @property
    def cards(self):
        return self._cards

    @property
    def clubs(self):
        return

    @property
    def spades(self):
        return

    @property
    def hearts(self):
        return

    @property
    def diamonds(self):
        return

    def suit(self, suit):
        return

    def number(self, number):
        return

class Hand(CardContainer):
    def __init__(self):
        pass

class Deck(CardContainer):
    def __init__(self):
        pass

    def shuffle(self):
        self._cards.shuffle