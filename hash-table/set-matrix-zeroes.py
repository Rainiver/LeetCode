class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zero_first_row = False
        zero_first_col = False
        
        # 遍历第一行
        for i in range(n):
            if matrix[0][i] == 0:
                zero_first_row = True
                break

        # 遍历第一列
        for i in range(m):
            if matrix[i][0] == 0:
                zero_first_col = True
                break
        
        # 步骤2：用第一行/列标记其他行/列的置零需求
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # 步骤3：根据标记，将非第一行/列置零
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if zero_first_row:
            for j in range(n):
                matrix[0][j] = 0
        if zero_first_col:
            for i in range(m):
                matrix[i][0] = 0
        
        return matrix
