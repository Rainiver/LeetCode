class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i] 考虑下标i以及之前的最大product
        n = len(nums)
        dp = [float('-inf')] * n
        dp[0] = nums[0]
        ans = dp[0]
        for i in range(1, n):
            dp[i] = max(dp[i], dp[i-1]*nums[i])
            ans = max(ans, dp[i])
        return ans