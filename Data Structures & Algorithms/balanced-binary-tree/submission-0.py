# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.height(root.left)+1, self.height(root.right)+1)
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if self.isBalanced(root.left) and self.isBalanced(root.right):
            return abs(self.height(root.right) - self.height(root.left)) < 2
        return False



        