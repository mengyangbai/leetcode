class Solution(object):
    def bestRotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        cnts = collections.defaultdict(int)
        ans = 0
        for i, n in enumerate(A):
            cnts[n - i] += 1
            ans += n <= i
        bestAns, bestIdx = ans, 0
        for x in range(len(A) - 1, -1, -1):
            y = len(A) - x - 1
            if A[x] <= x + y: ans -= 1
            if A[x] == 0: ans += 1
            cnts[A[x] - x] -= 1
            ans += cnts[y + 1]
            if ans >= bestAns:
                bestAns = ans
                bestIdx = x
            cnts[A[x] + y + 1] += 1
        return bestIdx
        