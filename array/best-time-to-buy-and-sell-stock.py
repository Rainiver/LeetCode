class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # dp[i][0]表示第i天持有这支股票的最多钱，dp[i][1]不持有这支股票的最多钱
        dp = [[0]*2 for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        profit = 0
        for i in range(1, len(prices)):
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
            dp[i][0] = max(dp[i-1][0], -prices[i])
            profit = max(profit, max(dp[i][1], dp[i][0]))
        return profit