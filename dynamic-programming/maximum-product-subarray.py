class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 由于存在负负得正，需要维护两个变量，分别为最大乘积和最小乘积
        # 计算最大乘积和最小乘积*当前元素的值，更新最大乘积和最小乘积。使用最大乘积更新结果
        # n = len(nums)
        ans = nums[0]
        max_pro, min_pro = ans, ans
        # 从第二个元素开始遍历（跳过已经初始化的第一个元素）
        for num in nums[1:]:
            pre_max, pre_min = max_pro, min_pro
            max_pro = max(num, pre_max*num, pre_min*num)
            min_pro = min(num, pre_max*num, pre_min*num)
            ans = max(ans, max_pro)
        return ans