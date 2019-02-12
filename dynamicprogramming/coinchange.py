class Solution:
    def change(self, amount: 'int', coins: '[int]') -> 'int':
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in coins:
            for j in range(i, amount + 1):
               if j >= i:
                   dp[j] += dp[j - i]
        
        return dp[-1]


a = Solution()
print(a.change(5,[1,2,5]))




