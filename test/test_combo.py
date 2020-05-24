import flush.combo as combo
from flush.deck import Card

def test_analyser_simple():

    def royal():
        cards = [
            Card('A', 'spades'),
            Card('K', 'spades'),
            Card('Q', 'spades'),
            Card('J', 'spades'),
            Card('10', 'spades')
        ]
        assert combo.HandAnalyser(cards).kind == 'SF'
    def straight_flush():
        cards = [
            Card('10', 'spades'),
            Card('9', 'spades'),
            Card('8', 'spades'),
            Card('7', 'spades'),
            Card('6', 'spades')
        ]
        assert combo.HandAnalyser(cards).kind == 'SF'
    def four():
        cards = [
            Card('A', 'spades'),
            Card('A', 'clubs'),
            Card('A', 'hearts'),
            Card('A', 'diamonds'),
            Card('K', 'spades')
        ]
        assert combo.HandAnalyser(cards).kind == '4K'
    def full():
        cards = [
            Card('A', 'spades'),
            Card('A', 'clubs'),
            Card('A', 'hearts'),
            Card('K', 'diamonds'),
            Card('K', 'spades')
        ]
        assert combo.HandAnalyser(cards).kind == 'FH'
    def flush():
        cards = [
            Card('A', 'spades'),
            Card('K', 'spades'),
            Card('4', 'spades'),
            Card('9', 'spades'),
            Card('7', 'spades')
        ]
        assert combo.HandAnalyser(cards).kind == 'FL'
    def straight():
        cards = [
            Card('A', 'spades'),
            Card('Q', 'clubs'),
            Card('J', 'hearts'),
            Card('10', 'diamonds'),
            Card('K', 'spades')
        ]
        assert combo.HandAnalyser(cards).kind == 'ST'
    def three():
        cards = [
            Card('A', 'spades'),
            Card('A', 'clubs'),
            Card('A', 'hearts'),
            Card('9', 'diamonds'),
            Card('K', 'spades')
        ]
        assert combo.HandAnalyser(cards).kind == '3K'
    def two():
        cards = [
            Card('A', 'spades'),
            Card('A', 'clubs'),
            Card('9', 'hearts'),
            Card('K', 'diamonds'),
            Card('K', 'spades')
        ]
        assert combo.HandAnalyser(cards).kind == '2P'
    def one():
        cards = [
            Card('A', 'spades'),
            Card('A', 'clubs'),
            Card('4', 'hearts'),
            Card('9', 'diamonds'),
            Card('K', 'spades')
        ]
        assert combo.HandAnalyser(cards).kind == '1P'
    def none():
        cards = [
            Card('A', 'spades'),
            Card('9', 'clubs'),
            Card('2', 'hearts'),
            Card('4', 'diamonds'),
            Card('K', 'spades')
        ]
        assert combo.HandAnalyser(cards).kind == 'NA'

    royal()
    straight_flush()
    four()
    full()
    flush()
    straight()
    three()
    two()
    one()
    none()

def test_analyser_competing():
    def straight_flush():
        royal = combo.HandAnalyser([
            Card('A', 'spades'),
            Card('K', 'spades'),
            Card('Q', 'spades'),
            Card('J', 'spades'),
            Card('10', 'spades')
        ])
    
        straight_flush = combo.HandAnalyser([
            Card('10', 'spades'),
            Card('9', 'spades'),
            Card('8', 'spades'),
            Card('7', 'spades'),
            Card('6', 'spades')
        ])

        assert royal.kind == 'SF'
        assert royal.kind == straight_flush.kind
        assert royal.opt > straight_flush.opt

    def flush():
        high = combo.HandAnalyser([
            Card('A', 'spades'),
            Card('K', 'spades'),
            Card('Q', 'spades'),
            Card('J', 'spades'),
            Card('9', 'spades')
        ])
    
        low = combo.HandAnalyser([
            Card('10', 'spades'),
            Card('9', 'spades'),
            Card('8', 'spades'),
            Card('5', 'spades'),
            Card('6', 'spades')
        ])

        assert high.kind == 'FL'
        assert high.kind == low.kind
        assert high.opt > low.opt

    straight_flush()
    flush()


if __name__ == "__main__":
    test_analyser_simple()