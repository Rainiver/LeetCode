import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[j]装满容量为j的背包最少的物品数量
        # dp[j] = min(dp[j - num**2], dp[j])  # num**2 小于j，否则无意义
        dp = [n+1] * (n+1)
        dp[0] = 0
        for i in range(1, n+1): # 背包容量
            for j in range(1, int(math.sqrt(i))+1):  # 物品数量
                if j**2 <= i:
                    dp[i] = min(dp[i], dp[i-j**2]+1)

        return dp[n]