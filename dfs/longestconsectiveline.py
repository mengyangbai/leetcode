class Solution:
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        
        if len(M) == 0:
            return 0
        
        dp = [[ [0, 0, 0, 0] for j in range(len(M[0]))] for i in range(len(M))]
        max_len = 0
        for row in range(len(M)):
            for col in range(len(M[0])):
                if M[row][col] == 1:
                    dp[row][col][0] = dp[row][col-1][0] + 1 if col > 0 else 1
                    dp[row][col][1] = dp[row-1][col][1] + 1 if row > 0 else 1
                    dp[row][col][2] = dp[row-1][col-1][2] + 1 if row > 0 and col > 0 else 1
                    dp[row][col][3] = dp[row-1][col+1][3] + 1 if row > 0 and col < len(M[0])-1 else 1

                max_len = max(max_len, dp[row][col][0], dp[row][col][1], dp[row][col][2], dp[row][col][3])
                
        return max_len

class badSolution:
    def longestLine(self, M: [[int]]) -> int:
        if not M:
            return 0

        def getres(i,j,m,n):
            if M[i][j] != 1:
                return 0
            elif i - m < len(M) and j - n < len(M[0]) and i - m >= 0 and j - n >= 0 and M[i-m][j-n] == 1:
                return 0                
            else:
                count = 1
                while i + m < len(M) and j + n < len(M[0]) and i + m >= 0 and j + n >= 0:
                    i = i + m
                    j = j + n

                    if M[i][j] != 1:
                        return count
                    else:
                        count+=1

                return count

        vectors = [[0,1],[1,0],[-1,1],[1,1]]

        res = 0
        for i in range(len(M)):
            for j in range(len(M[0])):
                for m,n in vectors:
                    res = max(res,getres(i,j,m,n))
            
        return res

a = Solution()
a.longestLine([[1,1,1]]
)

