import sys
import os
sys.path.append(os.path.join(sys.path[0], '..'))
from LeetCode.jump_game import Solution

def test_jump():
    s = Solution()
    assert s.canJump([2,3,1,1,4]) == True