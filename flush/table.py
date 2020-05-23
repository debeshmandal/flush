from deck import Deck, CardContainer

hands = {
    0: 'straight flush',
    1: 'four of a kind',
    2: 'full house',
    3: 'flush',
    4: 'straight',
    5: 'three of a kind',
    6: 'two pair',
    7: 'one pair',
    8: 'nothing'
}

class Target:
    def __init__(self):
        pass

    def collect(self, card_list):
        self.collection += card_list

class Player(Target):
    def __init__(self):
        pass

class Community(CardContainer, Target):
    def __init__(self):
        pass

class Burn(CardContainer, Target):
    def __init__(self):
        pass

class Dealer():
    def __init__(self, deck=Deck(), shuffle=True):
        self._deck = deck
        if shuffle:
            self._deck.shuffle

    def deal(self, n, target=None):
        cards = self._deck.deal(n)
        target.collect(cards)
        if target == None:
            return cards