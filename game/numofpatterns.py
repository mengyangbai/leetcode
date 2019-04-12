import collections
class Solution:
    cache = collections.Counter()
    def numberOfPatterns(self, m: int, n: int) -> int:
        if self.cache:
            return sum(self.cache[k] for k in range(m, n+1))
        
        visited = [False] * 10
        skip = {
            (1, 3): 2,
            (1, 7): 4,
            (3, 9): 6,
            (7, 9): 8,
            (2, 8): 5,
            (1, 9): 5,
            (3, 7): 5,
            (4, 6): 5,
        }
        skip = {frozenset(key): value for key, value in skip.items()}

        def dfs(key):
            visited[key] = True
            self.cache[sum(visited)] += 1
            for i in range(1, 10):
                if not visited[i]:
                    move = frozenset([key, i])
                    if move not in skip or visited[skip[move]]:
                        dfs(i)
            visited[key] = False
        
        for i in range(1, 10):
            dfs(i)
        
        return sum(self.cache[k] for k in range(m, n+1))