class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        dz = zip((1,0,-1,0),(0,1,0,-1))
        dp = [[0]* n for x in range(m)]
        dp[i][j] = 1
        ans = 0
        for t in range(N):
            ndp = [[0] * n for x in range(m)]
            for x in range(m):
                for y in range(n):
                    for dx,dy in dz:
                        nx,ny = x + dx, y+dy
                        if 0 <= nx < m and 0 <= ny <n:
                            ndp[nx][ny]= (ndp[nx][ny]+dp[x][y])%MOD
                        else:
                            ans = (ans + dp[x][y])% MOD
            
            dp = ndp
        
        return ans
