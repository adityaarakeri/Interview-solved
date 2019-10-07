import sys
import os
sys.path.append(os.path.join(sys.path[0], '..'))
from LeetCode.two_sum_II import twoSum

def test_twoSum():
    # check special cases
    assert twoSum([2, 7, 1, 15], 9) == [1, 2]

if __name__ == '__main__':
    test_twoSum()
    print('passed')
