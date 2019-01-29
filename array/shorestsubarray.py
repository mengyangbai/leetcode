class Solution:
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        length = len(A)
        # from 0 to x = dp
        dp = [0] * (length + 1)
        for i in range(length):
            dp[i+1] = dp[i] + A[i]
        
        res = length + 1
        monoq = []

        for i in range(len(dp)):

            while monoq and dp[i]<=dp[monoq[-1]]:
                monoq.pop()
            
            while monoq and dp[i]>=dp[monoq[0]]+K:
                res = min(res , i - monoq.pop(0))

            monoq.append(i)
        
        return res if res < length + 1 else -1

a = Solution()
print(a.shortestSubarray( [2,-1,2],3))


        
