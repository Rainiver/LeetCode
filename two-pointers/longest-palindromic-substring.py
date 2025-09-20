class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        ans = ""
        # 以每个字符为中心向2边展开
        for i in range(n):
            # 回文串为奇数个字符
            l, r= i-1, i+1
            while l >= 0 and r <=n-1 and s[l] == s[r]:
                l -= 1
                r += 1
            if len(ans) < r - l -1:
                ans = s[l+1:r]

            # 回文串为偶数个字符
            l, r= i, i+1
            while l >= 0 and r <=n-1 and s[l] == s[r]:
                l -= 1
                r += 1
            if len(ans) < r - l -1:
                ans = s[l+1:r]
        return ans