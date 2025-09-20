class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 当前房间偷不偷依赖于前一个房间和前两个房间偷不偷
        # dp[i]下标i（包含下标i之前的房间）能偷的最大金币，包括偷i和不偷i
        # dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        if n > 1:
            dp[1] = max(nums[0], nums[1])
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        
        return dp[n-1]
        