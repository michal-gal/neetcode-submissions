# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self,root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        main_list = []

        if root:
            queue.append(root)

        while len(queue) > 0:
            level_list = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                level_list.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            main_list.append(level_list)   

        return main_list


