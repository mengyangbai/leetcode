class Solution:
    def grayCode(self, n: int) -> [int]:
        sol = [0]
        for i in range(1, n+1):
            sol += [1<<i-1 | x for x in sol[::-1]]
        return sol  


