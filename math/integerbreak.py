class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * n
        for total in range(2, n + 1):
            for i in range(1, total//2 + 1):
                dp[total - 1] = max(dp[total - 1], max(dp[i - 1], i) * max(dp[total - i - 1], total - i))
        return dp[-1]

'''
class Solution {
    private static Map<Integer, Integer> small = new HashMap<>();
    private static Map<Integer, Integer> memo = new HashMap<>();

    static {
        small.put(1, 1);
        small.put(2, 1);
        small.put(3, 2);
    }

    public int integerBreak(int n) {
        if (n < 4)
            return small.get(n);
        else
            return helper(n);
    }

    public int helper(int n) {
        if (memo.get(n) != null)
            return memo.get(n);
        if (n == 2)
            return 2;
        else if (n == 3)
            return 3;
        else if (n < 2)
            return 1;
        else {
            int max = Math.max(2 * helper(n - 2), 3 * helper(n - 3));
            memo.put(n, max);
            return max;
        }
    }
}
'''