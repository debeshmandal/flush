import numpy as np
import pandas as pd
from typing import List
from .combo import HandAnalyser
from . import Registry

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
        _suit = '_' if self.suit == None else self.suit[0]
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
        return len(self.suit('clubs'))

    @property
    def spades(self):
        return len(self.suit('spades'))

    @property
    def hearts(self):
        return len(self.suit('hearts'))

    @property
    def diamonds(self):
        return len(self.suit('diamonds'))

    def suit(self, suit):
        return self.table[self.table['suit'].str.match(suit)]['value'].values

    def count(self, value):
        return self.table['value'].str.match(value).sum()

class Hand(CardContainer):

    def __init__(self, cards):
        CardContainer.__init__(self, cards)

    @property
    def analyser(self):
        return HandAnalyser(self)

    @property
    def kind(self):
        return self.analyser.kind

    @property
    def opt(self):
        return self.analyser.opt

    @property
    def score(self):
        kind_score = Registry().combos[self.kind]
        opt_score = self.opt / 1E-9
        score = kind_score + opt_score
        return score

    def __ge__(self, other):
        return self.score >= other.score 

    def __ne__(self, other):
        return self.score != other.score

    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score

    def __le__(self, other):
        return self.score <= other.score

    def __eq__(self, other):
        return self.score == other.score

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