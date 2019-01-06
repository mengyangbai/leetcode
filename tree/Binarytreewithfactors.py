import collections
class Solution:
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        dp = collections.defaultdict(int)
        MOD = 10 ** 9 + 7
        for i, a in enumerate(A):
            num = 0
            for j in range(i):
                m = A[j]
                if m * m > a: break
                if a % m: continue
                n = a / m
                num = (num + dp[m] * dp[n] * (1 + (m != n))) % MOD
            dp[a] = num + 1
        return sum(dp.values()) % MOD