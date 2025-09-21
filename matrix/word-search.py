class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        direct = [[0,1], [1,0], [0, -1], [-1, 0]]
        m = len(board)
        n = len(board[0])
        visited = [[False] * (n) for _ in range(m)]
        
        def dfs (x, y, idx):
            visited[x][y] = True
            if idx == len(word) - 1:
                    return True
            
            # 遍历四个方向
            for i in range(4):
                next_x = x + direct[i][0]
                next_y = y + direct[i][1]
                if 0 <= next_x < m and 0 <= next_y < n and board[next_x][next_y] == word[idx+1] and not visited[next_x][next_y]:
                    # 如果子递归找到路径则返回True
                    if dfs(next_x, next_y, idx+1):
                        return True
            # 回溯
            visited[x][y] = False
            # 四个方向都没找到，返回False
            return False    

        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False