class Solution:
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(n,i):
            if n == 1:
                return 1
            if i:
                return 2 * helper(n//2,0)
            elif n % 2 == 1:
                return 2 * helper(n//2,1)
            else:
                return 2 * helper(n//2,1) - 1

        return helper(n,1)

a = Solution()
print(a.lastRemaining(100000000))