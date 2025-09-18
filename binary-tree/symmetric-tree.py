# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def check(self, p, q):
        if (not p) and (not q):
            return True
        if (not p) or (not q) or p.val != q.val:
            return False
        return self.check(p.right, q.left) and self.check(p.left, q.right)
    
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.check(root.left, root.right)

    
        
        