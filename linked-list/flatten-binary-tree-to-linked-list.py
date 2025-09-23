# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        node = root
        while node:
            if node.left:
                tmp = node.left
                # 1. 找到左子树的最右节点（左子树前序遍历的尾节点）
                while tmp.right:
                    tmp = tmp.right
                # 2. 将原右子树接到这个尾节点的右子树。
                tmp.right = node.right
                # 3. 将左子树移到右子树位置，并清空左子树。
                node.right = node.left
                node.left = None
            node = node.right
        
        return node