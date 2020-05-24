from flush.deck import Deck, Hand
from flush import Registry
import random
import pandas as pd

def test_01(n=100):

    result = []

    # do simulation of 100,000 and see how many get which kind
    for i in range(n):
        hand = Hand(random.sample(Deck(), 7))
        result.append(hand.kind)

    pd.Series(result).value_counts().reindex(index = Registry().combos.keys()).to_csv('results.csv')

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        test_01(n=sys.argv[1])
    else:
        test_01()