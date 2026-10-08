# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lista = []
        if not root:
            return lista

        if root.left:
            for i in self.inorderTraversal(root.left):
                lista.append(i)
        lista.append(root.val)
        if root.right:
            for i in self.inorderTraversal(root.right):
                lista.append(i)
        return lista
        