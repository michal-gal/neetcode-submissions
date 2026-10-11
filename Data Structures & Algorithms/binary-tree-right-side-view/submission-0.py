# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self,root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        main_list = []

        if root:
            queue.append(root)
        while queue:
            q_len = len(queue)
            for i in range(q_len):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                print(main_list)
                if i == q_len - 1:
                    main_list.append(curr.val)



        return main_list