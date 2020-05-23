from deck import Deck, CardContainer

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