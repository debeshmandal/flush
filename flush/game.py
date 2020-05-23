from .deck import Hand

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

class Combo(Hand):
    def __init__(self, card_list):
        pass

    @staticmethod
    def is_possible(card_list):
        valid = []
        return [hands[i] for i in valid]

    @staticmethod
    def best_hand(card_list):
        return card_list
