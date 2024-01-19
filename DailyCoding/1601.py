"""
This question was asked by Apple.

Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

  10
 /  \
5    5
 \     \
   2    1
       /
     -1
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def min_path_sum(root):
    def dfs(node, current_sum):
        nonlocal min_sum
        if not node:
            return

        current_sum += node.val

        if not node.left and not node.right:  # If it's a leaf node
            min_sum = min(min_sum, current_sum)

        dfs(node.left, current_sum)
        dfs(node.right, current_sum)

    min_sum = float('inf')  # Initialize with positive infinity
    dfs(root, 0)

    return min_sum if min_sum != float('inf') else 0  # Return 0 for an empty tree

# Example usage:
# Constructing the given tree
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(5)
root.left.right = TreeNode(2)
root.right.right = TreeNode(1)
root.right.right.left = TreeNode(-1)

result = min_path_sum(root)
print("Minimum path sum:", result)
