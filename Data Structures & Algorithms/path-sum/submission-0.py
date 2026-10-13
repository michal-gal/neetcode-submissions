# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def leafPath(root, path, targetSum):
            if not root:
                return False
            self.path.append(root.val)
            self.sum += root.val

            if not root.left and not root.right and targetSum == self.sum:
                return True
            if leafPath(root.left, path, targetSum):
                return True
            if leafPath(root.right, path, targetSum):
                return True
            self.sum -= self.path.pop()
            return False

        self.path = []
        self.sum = 0
        return leafPath(root,self.path,targetSum)
