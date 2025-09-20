class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pivot = -1
        n = len(nums)
        for i in range(n-1, 0, -1):
            if nums[i-1] < nums[i]:
                pivot = i - 1
                break
        
        if pivot >= 0 :
            for i in range(n-1, pivot, -1):
                if nums[i] > nums[pivot]:
                    nums[i], nums[pivot] = nums[pivot], nums[i]
                    break   # 关键：交换后立即退出循环，避免多次交换

        l, r = pivot + 1, n-1
        while l < r:
           nums[l], nums[r] = nums[r], nums[l]  
           l += 1
           r -= 1
        
        return nums
