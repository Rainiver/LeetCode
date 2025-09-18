# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def build(self, nums, l, r):
        if l > r:
            return None

        mid = l + (r-l) // 2
        root = TreeNode(nums[mid])
        root.left = self.build(nums, l, mid - 1)
        root.right = self.build(nums, mid+1, r)
        return root

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        return self.build(nums, 0, len(nums)-1)
        