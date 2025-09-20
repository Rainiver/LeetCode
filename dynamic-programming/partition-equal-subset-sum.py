class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # dp[j]表示和为j的子集是否存在，分为选num和不选num
        # dp[j] = dp[j] or dp[j-num]
        total_sum = 0
        for num in nums:
            total_sum += num
        if total_sum%2 !=0 :
            return False
        n = total_sum // 2
        dp = [False] * (n+1)
        dp[0] = True # 基础条件：和为0必然能实现
        for num in nums: # 遍历物品
            for i in range(n, num-1, -1):  # 遍历背包容量
                dp[i] = dp[i] or dp[i-num]
        
        return dp[n]