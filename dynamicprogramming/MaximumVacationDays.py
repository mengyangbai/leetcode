class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        N, K = len(days), len(days[0])
        dp = [0] + [-1] * (N - 1)
        for w in range(K):
            ndp = [x for x in dp]
            for sc in range(N):
                if dp[sc] < 0: continue
                for tc in range(N):
                    if sc == tc or flights[sc][tc]:
                        ndp[tc] = max(ndp[tc], dp[sc] + days[tc][w])
            dp = ndp
        return max(dp)
        