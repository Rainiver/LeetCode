class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = []
        path = []
        n = len(s)
        def is_palin(l, r):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True        
        def dfs(idx):
            # 循环终止条件
            if idx == n:
                ans.append(path.copy())
                return 

            for i in range(idx, n):
                if is_palin(idx, i):
                    path.append(s[idx:i+1]) 
                    dfs(i+1)
                    # 回溯：
                    path.pop()

        dfs(0)
        return ans