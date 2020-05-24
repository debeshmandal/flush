from flush.deck import Deck, Hand
from flush import Registry
import random
import pandas as pd

def test_01():

    result = []

    # do simulation of 100,000 and see how many get which kind
    for i in range(10000):
        hand = Hand(random.sample(Deck(), 7))
        result.append(hand.kind)

    pd.Series(result).value_counts().reindex(index = Registry().combos.keys()).to_csv('results.csv')

if __name__ == '__main__':
    test_01()