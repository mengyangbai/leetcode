class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        n = len(prices)

        if n == 1:
            return 0

        dp = [0 for i in range(n + 1)]
        tmpmin = prices[0]
        for i in range(1, n + 1):
            tmpmin = min(tmpmin, prices[i - 1])
            tmpres = prices[i - 1] - tmpmin
            dp[i] = max(tmpres, dp[i - 1])

        return dp[-1]


a = Solution()
a.maxProfit([7, 1, 5, 3, 6, 4])
