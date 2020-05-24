import flush.deck as deck

def test_cards():
    deck.Card('A', 'spades')

    try:
        to_fail = deck.Card('ka', 'aido')
    except AssertionError:
        pass
    else:
        raise AssertionError

    assert deck.Card('A') > deck.Card('K')
    assert deck.Card('A') >= deck.Card('A')
    assert deck.Card('K') < deck.Card('A')
    assert deck.Card('A') <= deck.Card('A')
    assert deck.Card('A') != deck.Card('K')
    assert deck.Card('A') == deck.Card('A')

    cards = [
        deck.Card('2'), 
        deck.Card('J'), 
        deck.Card('K'),
        deck.Card('9'),
        deck.Card('6')
    ]

    assert sorted(cards)[0].value == '2'

def test_deck():
    assert deck.Deck().clubs == 13
    assert deck.Deck().hearts == 13
    assert deck.Deck().diamonds == 13
    assert deck.Deck().spades == 13
    for value in deck.Registry().values:
        assert deck.Deck().count(value) == 4
    assert isinstance(deck.Deck(), list)
    assert deck.Deck()[0] == deck.Card('A', 'hearts')

def test_hands():
    highest = deck.Hand([
            deck.Card('A', 'spades'),
            deck.Card('K', 'spades'),
            deck.Card('Q', 'spades'),
            deck.Card('J', 'spades'),
            deck.Card('10', 'spades')
        ])
    mid = deck.Hand([
            deck.Card('A', 'spades'),
            deck.Card('A', 'clubs'),
            deck.Card('Q', 'spades'),
            deck.Card('Q', 'diamonds'),
            deck.Card('8', 'spades')
        ])
    lowest = deck.Hand([
            deck.Card('A', 'spades'),
            deck.Card('5', 'clubs'),
            deck.Card('Q', 'spades'),
            deck.Card('2', 'spades'),
            deck.Card('8', 'spades')
        ])
    sorted([mid, lowest, highest])[0].kind == 'SF'

if __name__ == '__main__':
    test_cards()
    test_deck()
    test_hands()