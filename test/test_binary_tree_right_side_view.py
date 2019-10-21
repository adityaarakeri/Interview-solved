import sys
import os
sys.path.append(os.path.join(sys.path[0], '..'))
from LeetCode.binary_tree_right_side_view import Solution

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def test_binary_tree_right_side_view():

    root = TreeNode(1)
    
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(None)
    root.left.right = TreeNode(5)

    root.right.right = TreeNode(4)
    root.right.left = TreeNode(None)

    S = Solution()

    assert S.rightSideView(root) == [1, 3, 4]


