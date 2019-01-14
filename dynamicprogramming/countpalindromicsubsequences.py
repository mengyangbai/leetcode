class Solution:
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        wordlen = len(S)
        
        dp = [[0 for _ in range(wordlen)] for _ in range(wordlen)]
        
        for i in range(wordlen):
            dp[i][i] = 1
            
        for distance in range(1,wordlen):
            for i in range(wordlen-distance):
                j = i + distance

                if S[i] == S[j]:
                    low = i + 1
                    high = j - 1

                    while low <= high and S[low] != S[j]:
                        low += 1
                    
                    while low <= high and S[high] != S[j]:
                        high -= 1

                    if low > high:
                        dp[i][j] = dp[i+1][j-1] * 2 + 2
                    
                    elif low == high:
                        dp[i][j] = dp[i+1][j-1] * 2 + 1
                    
                    else:
                        dp[i][j] = dp[i+1][j-1] * 2 - dp[low+1][high-1]
                
                else:
                    dp[i][j] = dp[i][j-1]+dp[i+1][j] - dp[i+1][j-1]
                
                dp[i][j] = (dp[i][j] + 1000000007, dp[i][j] % 1000000007)[dp[i][j] >= 0]

        return dp[0][wordlen - 1]

a = Solution()
a.countPalindromicSubsequences("bccb")