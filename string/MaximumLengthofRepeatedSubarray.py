class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        sa, sb = len(A), len(B)
        dp = [0] * sb
        ans = 0
        for x in range(sa):
            ndp = [0] * sb
            for y in range(sb):
                if A[x] == B[y]:
                    ndp[y] = 1
                    if x and y:
                        ndp[y] += dp[y - 1]
                ans = max(ans, ndp[y])
            dp = ndp
        return ans
        