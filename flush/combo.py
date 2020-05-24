from collections import Counter

import numpy as np

from . import Registry

class HandAnalyser():
    def __init__(self, cards):
        self.cards = cards
        self._kind = self.kind
        del self._kind

    @staticmethod
    def binstr(values):
        string_list = np.zeros(13, dtype=np.int8)
        for value in values:
            index = Registry()._hierarchy[value]
            string_list[index] += 1
        string = ''.join(
                [str(i) for i in reversed(string_list)]
            )
        return string
    
    @property
    def kind(self):

        def groups(values):
            groups = list(Counter(values).items())
            return sorted(
                groups,
                key=lambda x: x[1],
                reverse=True
            )

        def is_straight(values):
            if len(values) < 5:
                return False
            _v = sorted([Registry().hierarchy[i] for i in sorted(values)])
            for i in range(0, len(values)-4):
                if _v[i+4] - _v[i] == 4:
                    return sorted(values)[i+4]
            else:
                return False
        
        def is_flush(suits):
            if len(suits) < 5:
                return False
            groups = list(Counter(suits).items())
            groups = sorted(
                groups,
                key=lambda x: x[1],
                reverse=True
            )
            if groups[0][1] >= 5:
                suit = groups[0][0]
                return list(self.cards.suit(suit))
            else:
                return False
        
        scores = {}
        group = groups(self.values)
        if group != []: 
            if group[0][1] == 4:
                scores['4K'] = int(HandAnalyser.binstr([group[0][0]]), 2)
            if group[0][1] == 3:
                if group[1][1] == 2:
                    scores['FH'] = int(HandAnalyser.binstr([group[0][0], group[1][0]]), 2)
                else:
                    scores['3K'] = int(HandAnalyser.binstr([group[0][0], group[1][0], group[2][0]]), 2)
            elif group[0][1] == 2:
                if group[1][1] == 2:
                    scores['2P'] = int(HandAnalyser.binstr([group[0][0], group[1][0], group[2][0]]), 2)
                else:
                    scores['1P'] = int(HandAnalyser.binstr([group[0][0], group[1][0], group[2][0], group[3][0]]), 2)
                    
        straight = is_straight(self.values)
        flush = is_flush(self.suits)

        if straight:
            if flush:
                scores['SF'] = int(HandAnalyser.binstr(flush), 2)
            else:
                scores['ST'] = int(HandAnalyser.binstr(straight), 2)
        elif flush:
            scores['FL'] = int(HandAnalyser.binstr(flush), 2)

        if len(scores.keys()) == 0:
            scores['NA'] = int(HandAnalyser.binstr(self.values), 2)
        val = sorted(
            scores.keys(),
            key=lambda x: Registry().combos[x])[0]
        self.opt = scores[val]
        return val

    @property
    def values(self):
        return [i.value for i in self.cards]

    @property
    def suits(self):
        return [i.suit for i in self.cards]