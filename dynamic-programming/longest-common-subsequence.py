class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # dp[i][j]表示 nums1[0, i-1]和 nums2[0, j-1]最长公共子序列的长度
        # 如果两数组末尾相同 if nums1[i-1] == nums2[j-1]: dp[i][j] = dp[i-1][j-1]+1 else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        m = len(text1)
        n = len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]