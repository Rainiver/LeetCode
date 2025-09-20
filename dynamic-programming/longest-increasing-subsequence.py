class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i]表示以nums[i]为结尾的最长子序列的长度
        # 注意subsequence是子序列不是字串，中间可以跳过一些元素，只要确保顺序不变就行。
        # nums[j] < nums[i]才有意义。for j in range(1, i): dp[i] = max(dp[i], dp[j]+1)

        n = len(nums)
        dp = [1] * n
        ans = 1
        
        for i in range(1, n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
            ans = max(ans, dp[i])
        return ans

        