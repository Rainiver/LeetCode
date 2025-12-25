class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
    
        res = [''] * numRows
        current_row = 0
        direction = -1  # 初始为-1，第一次循环会反转成+1（向下）
    
        for char in s:
            res[current_row] += char

            if current_row == 0 or current_row == numRows - 1:
                direction = -direction
            current_row += direction
    
        return ''.join(res)
        