class Solution(object):
    def sumSubseqWidths(self, A):
        s = diff = 0 
        k = 1 << max(len(A)-2,0)
        A.sort() 
        for i in range(len(A)):
            diff += A[~i] - A[i] 
            s += k * diff 
            k >>= 1 
        return s % (10 ** 9 + 7)


a =Solution()

a.sumSubseqWidths([2,1,3])