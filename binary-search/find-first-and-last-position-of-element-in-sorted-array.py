class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not len(nums):
            return [-1, -1]

        l, r = 0, len(nums) - 1
        # 找左边界
        while (l <= r):
            mid = (l+r) // 2
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        left = l   
        # 需要判断左边界是否越界     
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]
        
        l, r = 0, len(nums) - 1

        # 找右边界
        while (l <= r):
            mid = (l+r) //2
            if target < nums[mid]:
                r = mid -1
            else:
                l = mid + 1
        right = r
        
        return [left, right]   
        