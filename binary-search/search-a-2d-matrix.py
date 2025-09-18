class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m * n - 1
        
        while l <= r:
            mid = (l+r)//2
            if matrix[mid//n][mid%n] < target:
                l = mid + 1
            elif matrix[mid//n][mid%n] == target:
                return True
            else:
                r = mid -1
            
        # return matrix[l//n][l%n] == target
        return False

        