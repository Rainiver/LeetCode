class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        ans = []
        hashmap = [0] * 27
        for i in range(len(s)):
            hashmap[ord(s[i]) - ord('a')] = i
        l, r = 0, 0
        for i in range(len(s)):
            r = max(r, hashmap[ord(s[i])-ord('a')])
            if i == r:
                size = r - l + 1
                ans.append(size)
                l = i + 1
        
        return ans