# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def helper(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.helper(root.left)
        if left < 0:
            return -1
        right = self.helper(root.right)
        if right < 0:
            return -1
        if abs(left - right) > 1:
            return -1
        else:
            return max(left,right) + 1


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.helper(root) != -1
  



        