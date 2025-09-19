class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i, cover = 0, 0
        if len(nums) == 1:
            return True
        while i <= cover:
            cover = max(cover, i+nums[i])
            if cover >= len(nums)-1:
                return True
            i += 1
        return False