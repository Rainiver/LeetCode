# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_diameter = 0
    
        def depth(root):
            if not root:
                return 0
            self.max_diameter = max(self.max_diameter, depth(root.left)+depth(root.right))
        
            return max(depth(root.left), depth(root.right)) + 1
        
        depth(root)
        return self.max_diameter