import random

def test_random():
    randomlist = random.sample(range(1, 1000), 5)
    print(" ".join(map(str,randomlist)))
    return " ".join(map(str,randomlist))