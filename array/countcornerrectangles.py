class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        res = 0
        for x in range(m):
            for y in range(x+1,m):
                cnt = 0
                for z in range(n):
                    if grid[x][z] == 1 and grid[y][z] == 1:
                        cnt += 1
                    
                
                res += cnt * (cnt - 1) / 2

        return res