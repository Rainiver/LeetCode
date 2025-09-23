# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return root

        def dfs(node, left, right):
            if not node.left and not node.right:
                return
            
            # 交换左右节点，如何实现交换左右子树？
            node.left, node.right = node.right, node.left
            if node.left:
                tmp = node.left
                dfs(tmp, tmp.left, tmp.right)
            if node.right:
                tmp = node.right
                dfs(tmp, tmp.left, tmp.right)

        dfs(root, root.left, root.right)
        return root
