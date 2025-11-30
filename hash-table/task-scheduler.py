import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        tasks = ["A","A","A","B","B","B"], n = 2

        """
        hashmap = {}
        for task in tasks:
            if task not in hashmap:
                hashmap[task] = 1
            else:
                hashmap[task] += 1
        
        heap = [-cnt for cnt in hashmap.values() if cnt > 0]
        heapq.heapify(heap)
        queue = deque() # (cnt, next_time)
        time = 0

        while heap or queue:
            time += 1
            while queue and queue[0][1] == time:
                cnt, t = queue.popleft()
                heapq.heappush(heap, cnt)
            if heap:
                cnt1 = heapq.heappop(heap)
                cnt1 += 1
                if cnt1 < 0:
                    queue.append((cnt1, time + n + 1))
        
        return time


