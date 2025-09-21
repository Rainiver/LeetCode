class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        queue = []
        time = 0
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        # 第一步：初始化队列和新鲜橘子数
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i, j])
                elif grid[i][j] == 1:
                    fresh += 1

        # 第二步：多源BFS（按层处理，每一层对应1分钟）
        while queue and fresh > 0:
            level = len(queue)
            for _ in range(level):
                x, y = queue.pop(0) # 弹出队首元素（FIFO）
                # 向四周扩散
                for k in range(4):
                    next_x = x + direct[k][0]
                    next_y = y + direct[k][1]
                    if 0 <= next_x < m and 0 <= next_y < n and grid[next_x][next_y] == 1:
                        queue.append([next_x, next_y])
                        grid[next_x][next_y] = 2
                        fresh -= 1
            time += 1            
                    
        
        return time if fresh == 0 else -1
