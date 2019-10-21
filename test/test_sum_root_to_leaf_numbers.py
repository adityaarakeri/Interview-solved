import sys
import os
sys.path.append(os.path.join(sys.path[0], '..'))
from LeetCode.sum_root_to_leaf_numbers import Solution

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def test_sum_root_to_leaf_numbers():

    root = TreeNode(1)
    
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    S = Solution()

    assert S.sumNumbers(root) == 25
