'''

112. Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def path(self, root, t):
        if(root is None):
            return(t==0)
        else:
            
            ans = 0
            
            sub_sum = t - root.val
            
            if(sub_sum==0 and root.left is None and root.right is None):
                return(True)
            
            if(root.left is not None):
                ans = ans or self.path(root.left, sub_sum)
                
            if(root.right is not None):
                ans = ans or self.path(root.right, sub_sum)
                
            return ans

    
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
        if root is None:
            return(False)
        
        return(self.path(root, sum))




