class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        pos = [0] * 128
        ans = 0
        num_odd = 0
        for char in s:
            char_ord = ord(char)
            pos[char_ord] += 1
        for i in range(128):
            if pos[i] % 2 == 0:
                ans += pos[i]
            else:
                num_odd += 1
                ans += pos[i] - 1
        if num_odd >= 1:
            ans += 1
        return ans