class Registry():
    def __init__(self):
        self._values = ['A', 'K', 'Q', 'J'] + [str(10-i) for i in range(9)]
        self._suits = ['hearts', 'spades', 'clubs', 'diamonds']
        self._hierarchy = dict(zip(self._values, reversed(range(13))))
        self._combos = {
            'SF' : 0,
            '4K' : 1,
            'FH' : 2,
            'FL' : 3,
            'ST' : 4,
            '3K' : 5,
            '2P' : 6,
            '1P' : 7,
            'NA' : 8
        }

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