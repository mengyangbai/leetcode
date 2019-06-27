class Solution:
    def maxProfit(self, k, prices):
        n = len(prices)
        if n < 2:
            return 0
        if k >= n / 2:
            return sum(i - j
                    for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
        globalMax = [[0] * n for _ in range(k + 1)]
        for i in range(1, k + 1):
            localMax = [0] * n
            for j in range(1, n):
                profit = prices[j] - prices[j - 1]
                localMax[j] = max(
                    globalMax[i - 1][j - 1] + profit,
                    globalMax[i - 1][j - 1],  
                    localMax[j - 1] + profit)
                globalMax[i][j] = max(globalMax[i][j - 1], localMax[j])
        return globalMax[k][-1]
            


class BetterSolution:
    def maxProfit(self, k, prices):
        if k >= len(prices) // 2: return sum(sell - buy for sell, buy in zip(prices[1:], prices[:-1]) if sell - buy > 0)
        dp = [[0, -float("inf")] for _ in range(k + 1)]
        for p in prices:
            for i in range(k + 1):
                if i and dp[i - 1][1] + p > dp[i][0]: dp[i][0] = dp[i - 1][1] + p 
                if dp[i][0] - p > dp[i][1]: dp[i][1] = dp[i][0] - p
        return dp[-1][0]