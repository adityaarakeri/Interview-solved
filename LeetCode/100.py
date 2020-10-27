"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object): 
    def isSameTree(self, p, q):
        def checkTree(p, q):
            if p != None and q != None:
                if p.val != q.val:
                    return False
                l = checkTree(p.left, q.left)
                r = checkTree(p.right, q.right)
            elif p == None and q == None:
                return True
            else:
                return False
            if l == True and r == True:
                return True
            else:
                return False    
        
        return checkTree(p, q)
