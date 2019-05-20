class Solution:
	# @dp[x], sub-result for game N=x
	# @i, simulate the game N=i
	# @j, the factor we can take, filter by i % j == 0 to try all possible factors
    def divisorGame(self, N: int) -> bool:
        dp = [False for i in range(N+1)]
        for i in range(N+1):
             for j in range(1, i//2 + 1):
                    if i % j == 0 and (not dp[i - j]):
                        dp[i] = True
                        break
        return dp[N]