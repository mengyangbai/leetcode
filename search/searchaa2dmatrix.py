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


'''
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length ==0) return false;
        int row = 0;
        int col = matrix[0].length -1;
        while(row < matrix.length && col >= 0)
        {
            if(matrix[row][col] == target)
                return true;
            else if(matrix[row][col] > target)
                col--;
            else
                row++;
        }
        return false;
    }
}
'''