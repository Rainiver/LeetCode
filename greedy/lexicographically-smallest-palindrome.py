class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s_list = list(s)
        n = len(s)
        for i in range(n//2):
            j = n - 1 - i
            char = min(s[i], s[j])
            s_list[i] = char
            s_list[j] = char
        return "".join(s_list)
        