class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # 数组的初始化
        # dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        dp = []
        for i in range(numRows):
            row = [1] * (i+1)
            dp.append(row)
        for i in range(numRows):    
            for j in range(1, i):
               dp[i][j] = dp[i-1][j-1] + dp[i-1][j] 
        
        return dp

        
        
        