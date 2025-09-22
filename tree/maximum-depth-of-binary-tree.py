# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        depth = 0
        queue = [root]
        while queue:
            level_size = len(queue) # 记录当前层节点数量，处理完当前层depth才+1
            for i in range(level_size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # 处理完一层，深度+1
            depth += 1
        return depth


        