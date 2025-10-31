class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return nums
        l, r = 0, 0
        while r < len(nums):
            while r < len(nums) and nums[r] == 0:
                r += 1
            if r < len(nums) and nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1
            else:
                r += 1
        return nums