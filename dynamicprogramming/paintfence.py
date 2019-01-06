class Solution:
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        dp =[0,k,k*k,0]
        if n <= 2:
            return dp[n]
        
        for _ in range(2,n):
            dp[3] = (k-1) * (dp[1] + dp[2])
            dp[1] = dp[2]
            dp[2] = dp[3]
        
        return dp[3]
