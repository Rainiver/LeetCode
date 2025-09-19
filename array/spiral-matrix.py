class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        m = len(matrix)
        n= len(matrix[0])
        top, bottom, left, right = 0, m-1, 0, n-1
        while True:
            for col in range(left, right+1):
                res.append(matrix[top][col])
            top += 1
            if top > bottom:
                break

            for row in range(top, bottom+1):
                res.append(matrix[row][right])
            right -= 1
            if left > right:
                break 

            for col in range(right, left-1, -1):
                res.append(matrix[bottom][col])
            bottom -= 1
            if top > bottom:
                break

            for row in range(bottom, top-1, -1):
                res.append(matrix[row][left])
            left += 1
            if left > right:
                break
        
        return res