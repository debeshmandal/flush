from collections import Counter
from . import Registry

class HandAnalyser():
    def __init__(self, cards):
        self.cards = cards
    
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
            _v = [Registry().hierarchy(i) for i in sorted(values)]
            if _v[-1] - _v[0] == 4:
                return True
            else:
                return False
        
        def is_flush(suits):
            if len(values) < 5:
                return False
            groups = list(Counter(values).items())
            groups = sorted(
                groups,
                key=lambda x: x[1],
                reverse=True
            )
            if groups[0][1] >= 5:
                return True
            else:
                return False
            
        if groups(self.cards.values) != []: 
            if groups[0][1] == 3:
                if groups[1][1] == 2:
                    val = 'FH'
                else:
                    val = '3K'
            elif groups[0][1] == 2:
                if groups[1][1] == 2:
                    val = '2P'
                else:
                    val = '1P'
                    
        straight = is_straight(self.values)
        flush = is_flush(self.suits)

        if straight:
            if flush:
                val = 'SF'
            else:
                val = 'ST'
        elif flush:
            val = 'FL'

        val = 'NA'
        opts = []
        return val, opts

    @property
    def kickers(self):
        return 

    @property
    def values(self):
        return [i.value for i in self.cards]

    def suits(self):
        return [i.suit for i in self.cards]