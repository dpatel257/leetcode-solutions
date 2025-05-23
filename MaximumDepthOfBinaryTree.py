# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        if root and not root.left and not root.right:
            return 1
        
        return ( 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)))
