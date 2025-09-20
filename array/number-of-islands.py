class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        visited = [[False]*n for _ in range(m)]
        res = 0
        direct = [[0, 1], [1, 0], [-1, 0], [0, -1]] # 四个方向
        def dfs(grid, visited, x, y):
            for i in range(4):
                next_x = x + direct[i][0]
                next_y = y + direct[i][1]
                if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                    continue
                else:
                    if grid[next_x][next_y] == "1" and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        dfs(grid, visited, next_x, next_y)
                        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    res += 1
                    visited[i][j] = True
                    dfs(grid, visited, i, j)
        
        
        return res