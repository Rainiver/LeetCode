# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        if not root:
            return 0
        ans = 0
        
        def dfs(node, target):
            count = 0
            if not node:
                return count
            target -= node.val
            if target == 0:
                count += 1
            count += dfs(node.left, target)
            count += dfs(node.right, target)
            target += node.val
            return count

        # 枚举起点，用bfs
        queue = [root]
        while queue:
            item = queue.pop(0)
            if item:
                queue.append(item.left)
                queue.append(item.right)
                ans += dfs(item, targetSum)
       
        return ans

