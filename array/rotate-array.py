class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 3次旋转法，1:翻转整个数组；2:翻转前k个；3:翻转后n-k个
        n = len(nums)
        k = k % n
        def reverse(nums, l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            return nums
        nums = reverse(nums, 0, n-1)
        nums = reverse(nums, 0, k-1)
        nums = reverse(nums, k, n-1)

        return nums