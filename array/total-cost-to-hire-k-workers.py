class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        
        # 两个最小堆
        head_heap = []
        tail_heap = []
        
        # 双指针，指向中间"未进入候选池"区域的左右边界
        # next_head 指向左边下一个待进入的元素
        # next_tail 指向右边下一个待进入的元素
        next_head = 0
        next_tail = n - 1
        
        # 1. 初始化左堆
        # 注意边界：不能超过 candidates，且不能越过右边的指针(防止数组很短时重复添加)
        while next_head < candidates and next_head <= next_tail:
            heapq.heappush(head_heap, costs[next_head])
            next_head += 1
            
        # 2. 初始化右堆
        # 注意边界：需要填满 candidates 个，且不能越过左边的指针
        # 这里的条件逻辑：只要右堆没满，且指针没撞上 next_head (next_head-1是左堆最后一个元素)
        while len(tail_heap) < candidates and next_tail >= next_head:
            heapq.heappush(tail_heap, costs[next_tail])
            next_tail -= 1
            
        total_cost = 0
        
        # 3. 开始招人，循环 k 次
        for _ in range(k):
            # 比较两个堆顶
            # 为了处理堆可能为空的情况，我们将无穷大 float('inf') 作为默认值
            head_min = head_heap[0] if head_heap else float('inf')
            tail_min = tail_heap[0] if tail_heap else float('inf')
            
            # 如果左边更小或相等 (题目要求相等选下标小的，左边天然下标小)
            if head_min <= tail_min:
                total_cost += heapq.heappop(head_heap)
                
                # 补货：如果中间还有人
                if next_head <= next_tail:
                    heapq.heappush(head_heap, costs[next_head])
                    next_head += 1
            else:
                total_cost += heapq.heappop(tail_heap)
                
                # 补货：如果中间还有人
                if next_head <= next_tail:
                    heapq.heappush(tail_heap, costs[next_tail])
                    next_tail -= 1
                    
        return total_cost
        