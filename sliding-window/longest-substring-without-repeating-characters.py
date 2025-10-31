class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        l, r = 0, 0
        ans = 0
        pos = [0] * 128
        for char in s:
            char_ord = ord(char)
            
            l = max(l, pos[char_ord])
            pos[char_ord] = r
            ans = max(ans, r - l)
            r += 1
        return ans
