class Solution:
    def countBits(self, num: 'int') -> '[int]':
        dp = [0] * (num + 1)
        for i in range(1,len(dp)):
            dp[i] = dp[i & (i-1)]  + 1
        return dp