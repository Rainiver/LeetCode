class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        n = len(intervals)
        if n == 1:
            return intervals
        intervals.sort(key=lambda x:x[0])
        l, r = intervals[0][0], intervals[0][1]
        for i in range(1, n):
            if intervals[i][0] <= r:
                r = max(r, intervals[i][1])
            else:
                ans.append([l, r])
                l = intervals[i][0]
                r = intervals[i][1]
        ans.append([l, r])
        return ans
