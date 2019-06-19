class Solution:
    def isIdealPermutation(self, A):
        cmax = 0
        for i in range(len(A) - 2):
            cmax = max(cmax, A[i])
            if cmax > A[i + 2]:
                return False
        return True

class BestSolution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        for i, n in enumerate(A):
            if abs(i-n) > 1: return False
        return True