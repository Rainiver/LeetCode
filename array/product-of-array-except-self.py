class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix, post = 1,1
        n = len(nums)
        ans = [1] * n
        # 从前往后遍历前缀积
        for i in range(1, n):
            prefix = prefix * nums[i-1]
            ans[i] = prefix
            
        # 从后往前遍历后缀积
        for i in range(n-2, -1, -1):
            post = post * nums[i+1]
            ans[i] *= post
        
        return ans