def getGroup(nums, target):
    res, tmpsum, i = 1, 0, 0

    while i < len(nums):
        tmpsum = nums[i] + tmpsum
        if tmpsum > target:
            tmpsum = 0
            res = res + 1
        else:
            i = i + 1

    return res


class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        start = max(nums)
        end = sum(nums)

        while start < end:
            mid = (start + end) >> 1
            x = getGroup(nums, mid)
            if x > m:
                start = mid + 1
            elif x < m:
                end = mid
            else:
                end = mid

        return start

    def splitArray2(self, nums, m):
        n = len(nums)
        sums = [0] * (n + 1)
        dp = [[5000 for i in range(n + 1)] for j in range(m + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            sums[i] = sums[i - 1] + nums[i - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for k in range(i - 1, j, i):
                    val = max(dp[i - 1][k], sums[j] - sums[k])
                    dp[i][j] = min(dp[i][j], val)

        return dp[m][n]

    # int splitArray(vector<int>& nums, int m) {
    #     int n = nums.size();
    #     vector<int> sums(n + 1, 0);
    #     vector<vector<int>> dp(m + 1, vector<int>(n + 1, INT_MAX));
    #     dp[0][0] = 0;
    #     for (int i = 1; i <= n; ++i) {
    #         sums[i] = sums[i - 1] + nums[i - 1];
    #     }
    #     for (int i = 1; i <= m; ++i) {
    #         for (int j = 1; j <= n; ++j) {
    #             for (int k = i - 1; k < j; ++k) {
    #                 int val = max(dp[i - 1][k], sums[j] - sums[k]);
    #                 dp[i][j] = min(dp[i][j], val);
    #             }
    #         }
    #     }
    #     return dp[m][n];
    # }


a = Solution()

nums = [7, 2, 5, 10, 8]
m = 2

print(a.splitArray2(nums, m))
