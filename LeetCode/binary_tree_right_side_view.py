'''
199. Binary Tree Right Side View
Medium

1349

73

Favorite

Share
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def helper(self, root, level, max_level):
        
        if root is None:
            return
        
        if(max_level[0] < level):
            self.ans.append(root.val)
            max_level[0] = level
            
        self.helper(root.right, level+1, max_level)
        self.helper(root.left, level+1, max_level)
    
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        max_level = [0]
        self.ans = []
        self.helper(root, 1, max_level)
        
        return(self.ans)