import sys
import os
sys.path.append(os.path.join(sys.path[0], '..'))
from LeetCode.number_of_1_bits import Solution

def test_191():
    s = Solution()
    # check special cases
    assert s.hammingWeight(0) == 0
    assert s.hammingWeight(0b00000000000000000000000000001011) == 3
    assert s.hammingWeight(0b11111111) == 8

