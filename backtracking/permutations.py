class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        used = [False] * n
        ans = []
        per = []
        def dfs(nums, idx, used):
            # 递归终止条件
            if len(per) == n:
                ans.append(list(per))
                return
            
            for i in range(n):
                if used[i] == False:
                    used[i] = True
                    per.append(nums[i])
                    dfs(nums, idx+1, used)
                    # 回溯，恢复现场
                    per.pop()
                    used[i] = False




        dfs(nums, 0, used)
        
        return ans