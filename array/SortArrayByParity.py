class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        l, r = 0, len(A) - 1
        while l < r:
            while A[l] % 2 == 0 and l < r:
                l += 1
            while A[r] % 2 != 0 and l < r:
                r -= 1
            temp = A[l]
            A[l] = A[r]
            A[r] = temp
            l += 1
            r -= 1
        return A
        