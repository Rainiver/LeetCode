class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 字符串长度为i，dp[i] 是否为 true
        # dp[i] = dp[j] and s[i-j] in wordDict
        # dp[0] 一定要为True，否则后面全是False
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(0, i+1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True

        return dp[n]
        