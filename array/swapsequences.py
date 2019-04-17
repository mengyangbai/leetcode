class Solution:
    def minSwap(self, A: [int], B: [int]) -> int:
        swap, keep = 1, 0
        for i in range(1, len(A)):
            if A[i] <= A[i - 1] or B[i] <= B[i - 1]:
                # swap
                nswap = keep + 1
                nkeep = swap
            elif A[i] > B[i - 1] and B[i] > A[i - 1]:
                # swap or keep
                nkeep = min(keep, swap)
                nswap = nkeep + 1
            else:
                # keep
                nkeep = keep
                nswap = swap + 1
            swap, keep = nswap, nkeep
        return min(swap, keep)