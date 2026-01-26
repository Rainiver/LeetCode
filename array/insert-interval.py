class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        n = len(intervals)
        intervals.sort()
        res = []
        l, r = intervals[0][0], intervals[0][1]
        for i in range(1, n):
            if l <= intervals[i][0] <= r and intervals[i][1] >= r:
                r = intervals[i][1]
            elif l <= intervals[i][0] <= r and intervals[i][1] < r:
                continue
            else:
                res.append([l, r])
                l = intervals[i][0]
                r = intervals[i][1]
        if l == intervals[n-1][0] and r == intervals[n-1][1]:
            res.append([l, r])
        return res

        