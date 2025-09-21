class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort(key = lambda x:x[0])
        ans = []
        n = len(intervals)
        l = intervals[0][0]
        r = intervals[0][1]
        for i in range(1, n):
            # 有重叠部分，合并区间
            if intervals[i][0] <= r:
                r = intervals[i][1]
            # 无重叠部分，左右边界加入答案并更新
            else:
                ans.append([l,r])
                l = intervals[i][0]
                r = intervals[i][1]
        ans.append([l,r])
        return ans
        