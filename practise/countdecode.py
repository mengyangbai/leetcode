class Solution(object):
    def getNum(self, t):
        if int(t) < 27:
            return 1
        else:
            return 0

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s:
            return 0

        s = str(s)
        n = len(s)
        dp = [1 for _ in range(n + 1)]
        for i in range(2, len(dp)):
            dp[i] = dp[i - 1] + dp[i - 2] * self.getNum(s[i - 2:i])

        return dp[-1]


a = Solution()

a.numDecodings(12)