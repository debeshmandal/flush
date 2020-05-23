import numpy as np
import pandas as pd
from typing import List

class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class CardContainer:
    def __init__(self, cards : List[Card]):
        self._cards = cards
        self._cards_df = pd.DataFrame(cards, columns = ['value', 'suit'])

    @property
    def N(self):
        return len(self.cards)

    @property
    def cards(self):
        return self._cards

    @property
    def clubs(self):
        return self.suit('clubs')

    @property
    def spades(self):
        return self.suit('spades')

    @property
    def hearts(self):
        return self.suit('hearts')

    @property
    def diamonds(self):
        return self.suit('diamonds')

    def suit(self, suit):
        return

    def number(self, number):
        return

class Hand(CardContainer):
    def __init__(self):
        pass

class Deck(CardContainer):
    def __init__(self):
        self._cards = Deck.generate()

    @staticmethod
    def generate():
        cards = []
        return cards

    def shuffle(self):
        self._cards.shuffle