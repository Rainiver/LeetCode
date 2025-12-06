class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        ans = [[0]*c for _ in range(r)]
        if r * c != m * n:
            return mat
        for i in range(m):
            for j in range(n):
                idx = n * i + j
                row = idx // c
                col = idx % c
                ans[row][col] = mat[i][j]
        
        return ans 
        
        