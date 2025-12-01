import heapq
from collections import deque
class Solution:
    def reorganizeString(self, s: str) -> str:
        # n = 1 的task schedular
        hashmap = {}
        heap = []
        queue = deque()
        res = ""
        
        for char in s:
            if char not in hashmap:
                hashmap[char] = 1
            else:
                hashmap[char] += 1

        for key, value in hashmap.items():
            heapq.heappush(heap, (-value, key)) 
        time = 0
        while heap or queue:
            time += 1
            
            while queue and queue[0][2] == time:
                char, freq, t = queue.popleft()
                heapq.heappush(heap, (-freq, char))
                
            if heap:
                freq, char = heapq.heappop(heap)
                res += char
                freq += 1
                if freq < 0:
                    queue.append((char, freq, time + 2))
                
        if len(res) == len(s):
            return res   
        else:
            return ""
        