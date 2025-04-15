# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # If both nodes are empty, they are identical
        if p is None and q is None:
            return True
        
        # If only one of them is empty, it is a mismatch
        if p is None or q is None:
            return False
        
        # If certain node compares same, call tree comparision for both left and right child
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

