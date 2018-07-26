class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target

    # @return a boolean
    def searchMatrix(self, matrix, target):
        i = 0
        if i == 0:
            return False
        j = len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False


a = Solution()
a.searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5)
