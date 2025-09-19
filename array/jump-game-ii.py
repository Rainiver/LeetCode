class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        res = 0
        cur_cover = 0
        next_cover = 0
        for i in range(len(nums)):
            # 更新下一步能覆盖的最远边界
            next_cover = max(next_cover, i + nums[i])
            
            # 当到达当前覆盖范围的边界时，需要跳跃
            if i == cur_cover:
                res += 1
                cur_cover = next_cover
                # 如果当前覆盖范围已包含终点，提前退出
                if cur_cover >= len(nums)-1:
                    break
        
        return res

        