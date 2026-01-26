class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        n = len(intervals)
        intervals.sort()
        res = []
        l, r = intervals[0][0], intervals[0][1]
        for i in range(1, n):
            if l <= intervals[i][0] <= r :
                r = max(r, intervals[i][1])
            else:
                res.append([l, r])
                l = intervals[i][0]
                r = intervals[i][1]
        
        res.append([l, r])
        return res

        