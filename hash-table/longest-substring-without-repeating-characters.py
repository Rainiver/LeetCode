class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        l, r = 0, 0
        ans = 1
        pos = [0] * 128
        for char in s:
            char_ord = ord(char)
            
            l = max(l, pos[char_ord]+1)
            pos[char_ord] = r
            ans = max(ans, r - l+1)
            r += 1
            
        return ans
