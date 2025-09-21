class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        
        def dfs(l, r, path):
            # 递归终止条件
            if l == n and r == n:
                ans.append(path)
                return
            # 左括号都能加
            if l < n:
                dfs(l+1, r, path+"(")
                # path自动恢复为原来的，无需手动回溯
            if  l<=n and r < l:
                dfs(l, r+1, path+")")
                # path自动恢复为原来的，无需手动回溯

        dfs(0, 0,  "")
        return ans
        