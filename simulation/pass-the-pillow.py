class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle = 2* (n-1)
        ans = time % cycle
        if ans < n:
            return ans + 1
        else:
            return 2 * (n-1) - (ans - 1)


        