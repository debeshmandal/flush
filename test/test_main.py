from flush import Registry

def test_registry():
    values = Registry().values
    suits = Registry().suits
    hierarchy = Registry().hierarchy
    assert 'hearts' in suits
    assert 'spades' in suits
    assert 'clubs' in suits
    assert 'diamonds' in suits
    assert hierarchy['A'] > hierarchy['J']
    
if __name__ == '__main__':
    test_registry()