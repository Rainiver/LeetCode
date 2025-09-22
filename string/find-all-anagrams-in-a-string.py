class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_count = [0] * 26
        s_count = [0] * 26
        ans = []
        for char in p:
            p_count[ord(char)-ord("a")] += 1
        n_p = len(p)
        l, r = 0, n_p-1
        n = len(s)
        if n_p > n:
            return ans
        for i in range(n_p):
            s_count[ord(s[i])-ord("a")] += 1
        if s_count == p_count:
                ans.append(l)

        while r < n-1:
            s_count[ord(s[l])-ord("a")] -= 1
            l += 1
            r += 1
            s_count[ord(s[r])-ord("a")] += 1
            
            if s_count == p_count:
                ans.append(l)

        return ans
        