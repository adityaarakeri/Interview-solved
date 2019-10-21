import sys
import os
sys.path.append(os.path.join(sys.path[0], '..'))
from LeetCode.path_sum import Solution

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def test_path_sum():

    root = TreeNode(5)
    
    root.left = TreeNode(4)
    root.right = TreeNode(8)

    root.left.left = TreeNode(11)

    root.right.right = TreeNode(13)
    root.right.left = TreeNode(4)

    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)

    root.right.left.right = TreeNode(1)

    S = Solution()

    assert S.hasPathSum(root, 22) == True

