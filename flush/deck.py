import numpy as np
import pandas as pd
from typing import List

class Registry():
    def __init__(self):
        self._values = ['A', 'K', 'Q', 'J'] + [str(10-i) for i in range(9)]
        self._suits = ['hearts', 'spades', 'clubs', 'diamonds']
        self._hierarchy = dict(zip(self._values, reversed(range(13))))

    @property
    def values(self):
        return self._values

    @values.getter
    def values(self):
        return self._values
    
    @property
    def suits(self):
        return self._suits
    
    @suits.getter
    def suits(self):
        return self._suits

    @property
    def hierarchy(self):
        return self._hierarchy

    @hierarchy.getter
    def hierarchy(self):
        return self._hierarchy

class Card():
    def __init__(self, value, suit=None):
        assert value in Registry().values
        if suit != None:
            assert suit in Registry().suits
        self.value = value
        self.suit = suit
    
    @property
    def hierarchy(self):
        return Registry().hierarchy[self.value]

    def __ge__(self, other):
        return self.hierarchy >= other.hierarchy 

    def __ne__(self, other):
        return self.hierarchy != other.hierarchy

    def __lt__(self, other):
        return self.hierarchy < other.hierarchy

    def __gt__(self, other):
        return self.hierarchy > other.hierarchy

    def __le__(self, other):
        return self.hierarchy <= other.hierarchy

    def __eq__(self, other):
        return self.hierarchy == other.hierarchy

    def __repr__(self):
        _suit = '_' if self.suit == None else self.suit
        return f"{self.value}{_suit}"

class CardContainer(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.table = self.dataframe(self)

    @staticmethod
    def dataframe(cards):
        df = pd.DataFrame(
            {
                'value' : [i.value for i in cards],
                'suit' : [i.suit for i in cards]
            }
        )
        return df

    @property
    def N(self):
        return len(self)

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
        return self.table['suit'].str.match(suit).sum()

    def count(self, value):
        return self.table['value'].str.match(value).sum()

class Hand(CardContainer):
    def __init__(self):
        CardContainer.__init__(self, [])

class Deck(CardContainer):
    def __init__(self, shuffle=False):
        CardContainer.__init__(self, self.generate())
        if shuffle:
            self.shuffle()

    @staticmethod
    def generate():
        _cards = []
        for i in Registry().values:
            for j in Registry().suits:
                _cards.append(Card(i, j))
        return _cards

    def shuffle(self):
        self._cards.shuffle()