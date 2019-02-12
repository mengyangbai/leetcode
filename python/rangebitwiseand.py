class Solution:
    def rangeBitwiseAnd(self, m, n):
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i


a = Solution()
print(a.rangeBitwiseAnd(5,7))