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
            node = queue.pop(0)
            level_size -= 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if level_size == 0:
                depth += 1
        return depth


        