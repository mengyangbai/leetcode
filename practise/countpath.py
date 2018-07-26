class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1 for i in range(m)] for j in range(n)]

        for j in range(1, n):
            for i in range(1, m):
                dp[j][i] = dp[j][i - 1] + dp[j - 1][i]

        return dp[-1][-1]


a = Solution()
a.uniquePaths(3, 2)
