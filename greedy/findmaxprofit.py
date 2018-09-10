class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        def findKey(lis, key):
            left, right = 0, len(lis)-1
            while left < right:
                mid = (left+right) // 2
                if lis[mid] < key < lis[mid+1]:
                    return lis[mid]
                elif key < lis[mid] and key < lis[mid+1]:
                    right = mid
                elif key > lis[mid] and key > lis[mid+1]:
                    left = mid
                
        dp = sorted(zip(difficulty, profit))
        for i in range(1, len(dp)):
            dp[i] = (dp[i][0], max(dp[i-1][1], dp[i][1]))
        ans = 0
        dp = dict(dp)
        sorted_d = sorted(difficulty)
        min_dp = min(dp)
        max_dp = max(dp)
        for w in worker:
            if w >= min_dp:
                if w in dp:
                    ans += dp[w]
                elif w > max_dp:
                    ans += dp[max_dp]
                else:
                    ans += dp[findKey(sorted_d, w)]
        return ans
        