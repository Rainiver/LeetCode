# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        ans = []
        ans.append([root.val])
        while queue:
            cur_value = []
            level = len(queue)
            for i in range(level):
                item = queue.pop(0)
                if item.left:
                    cur_value.append(item.left.val)
                    queue.append(item.left)
                if item.right:
                    cur_value.append(item.right.val)
                    queue.append(item.right)
            if cur_value:
                ans.append(cur_value)
            
        return ans