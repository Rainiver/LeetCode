class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        path = []
        n = len(nums)
        def dfs(idx, nums):
            # 关键修正1：每次进入递归就记录当前子集（包括空集和所有中间状态）
            ans.append(list(path))
            
            # 从当前索引idx开始选择，确保顺序
            for i in range(idx, n):
                # 选当前元素 nums[i]
                path.append(nums[i])
                dfs(i+1, nums)
                # 回溯：撤销选择，尝试“不选当前元素”的分支
                path.pop()



        dfs(0, nums)

        return ans
        