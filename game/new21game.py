"""
    Use dp to solve this
"""
class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        if K == 0: return 1
        dp = [1.0] + [0] * N
        tSum = 1.0
        for i in range(1, N + 1):
            dp[i] = tSum / W
            if i < K:
                tSum += dp[i]
            if 0 <= i - W < K:
                tSum -= dp[i - W]
        return sum(dp[K:])
