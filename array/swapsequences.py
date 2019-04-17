class Solution:
    def minSwap(self, A: [int], B: [int]) -> int:
        n = len(A)
        noswap = [float('inf')] * n
        swap = [float('inf')] * n
        noswap[0] = 0
        swap[0] = 1

        for i in range(1,n):
            if A[i-1] < A[i] and B[i-1] < B[i]:
                swap[i] = swap[i-1] + 1
                noswap[i] = noswap[i-1]
            
            if A[i] > B[i-1] and B[i] > A[i-1]:
                swap[i] = min(swap[i],noswap[i-1]+1)
                noswap[i] = min(noswap[i],swap[i-1])

        return min(swap[i-1],noswap[i-1])