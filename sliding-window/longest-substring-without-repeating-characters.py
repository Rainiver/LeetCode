class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        pos = [-1]*128
        l, r = 0, 0
        for char in s:
            char_code = ord(char)
            l = max(l, pos[char_code] + 1)
            ans = max(ans, r - l + 1)
            pos[char_code] = r
            r += 1
        return ans
