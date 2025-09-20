class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount+1] * (amount+1)
        # dp[j]装满容量为j的背包的最少物品数量
        # dp[j] = min(dp[j- num[i]]+1, dp[j])
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                dp[i] = min(dp[i-coin]+1, dp[i])
        
        # 注意如果凑不出来的话表示dp数组没有更新，返回-1
        
        return dp[amount] if dp[amount] != amount+1 else -1
        