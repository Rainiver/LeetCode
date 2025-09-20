class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 延续前面的子序列 or 从这里从头开始计算
        # dp[i] = max(nums[i], dp[i-1]+nums[i])
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        ans = dp[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
            ans = max(ans, dp[i])
        return ans