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
            _v = sorted([Registry().hierarchy[i] for i in sorted(values)])
            if _v[-1] - _v[0] == 4:
                return True
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
                return True
            else:
                return False
        
        val = []
        group = groups(self.values)
        if group != []: 
            if group[0][1] == 4:
                val.append('4K')
            if group[0][1] == 3:
                if group[1][1] == 2:
                    val.append('FH')
                else:
                    val.append('3K')
            elif group[0][1] == 2:
                if group[1][1] == 2:
                    val.append('2P')
                else:
                    val.append('1P')
                    
        straight = is_straight(self.values)
        flush = is_flush(self.suits)

        if straight:
            if flush:
                val.append('SF')
            else:
                val.append('ST')
        elif flush:
            val.append('FL')

        val.append('NA')
        val = sorted(
            val,
            key=lambda x: Registry()._combos[x])
        return val[0]

    @property
    def values(self):
        return [i.value for i in self.cards]

    @property
    def suits(self):
        return [i.suit for i in self.cards]