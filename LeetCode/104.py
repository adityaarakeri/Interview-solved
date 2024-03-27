"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def max_depth(self, root: Optional(TreeNode)) -> int:
        # creating a stack with the root and the initial level depth
        stack = [[root, 1]]
        result = 0

        # while the stack exists
        while stack:
            # start popping the stack
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                # increasing the depth if we know node exists
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
            
        return result

q1 = [3,9,20,None,None,15,7]
s = Solution()
node = TreeNode()
node.val = 3
node.left = 9
node.right = 20

