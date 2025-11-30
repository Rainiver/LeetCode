# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        queue = deque([root])
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                item = queue.popleft()
                if item and item.left:
                    queue.append(item.left)
                if item and item.right:
                    queue.append(item.right)
                if i == level_size - 1 and item:
                    res.append(item.val)
        return res


        