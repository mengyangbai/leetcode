class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        m = len(matrix)
        n = len(matrix[0])

        x = n - 1
        y = 0
        while y < m and x >= 0:
            tmp = matrix[y][x]
            if tmp == target:
                return True
            if tmp > target:
                x = x - 1
            else:
                y = y + 1

        
        return False