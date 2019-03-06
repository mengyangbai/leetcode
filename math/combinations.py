import itertools
class Solution:
    def combine(self, n: 'int', k: 'int') -> '[[int]]':
        """
        Recursive algorithm.
        """
        if n < k:
            return []
        if k == 0:
            return [[]]
        
        def helper(alist, k):
            if k == 1:
                res = []
                for num in alist:
                    res.append([num])
                return res
            
            if k > 1:
                res = []
                for i in range(0, len(alist)-k+1):
                    alist_i = alist[i+1:]
                    for comb in helper(alist_i, k-1):
                        res.append([alist[i]] + comb)
                return res
    
        return helper(list(range(1, n+1)), k)


class Solution:
    def combine(self, n: int, k: int) -> [[int]]:
        res = []
        for single in itertools.combinations(range(1,n+1),k):
            res.append(list(single))
        return res

a = Solution()
print(list(a.combine(4,2)))

