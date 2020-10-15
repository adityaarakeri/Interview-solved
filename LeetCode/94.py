#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Input: root = [1,null,2,3]
Output: [1,3,2]
Explanation: Iteration with stack

'''

from typing import List
# Definition for a binary tree node.
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

# Iteration-based solution
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        res = []
        stk = []
        
        while root or len(stk) != 0:
            while root is not None:
                stk.append(root)
                root = root.left
                
            root = stk[-1]
            res.append(root.val)
            stk.pop()
            root = root.right

        return res

root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
s = Solution()
print(s.inorderTraversal(root))
