import sys
import os
sys.path.append(os.path.join(sys.path[0], '..'))
from Company.letter_count import letter_count


def test_letter_count():
    assert letter_count("arithmetics") == {"a": 1, "c": 1, "e": 1, "h": 1, "i": 2, "m": 1, "r": 1, "s": 1, "t": 2}

if __name__ == '__main__':
    test_letter_count()
