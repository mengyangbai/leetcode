class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        parent = {chr(ord('a') + i): chr(ord('a') + i) for i in range(26)}
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx < ry:
                parent[ry] = rx
            elif rx > ry:
                parent[rx] = ry
        
        for x, y in zip(A, B):
            union(x, y)
            
        return ''.join(find(c) for c in S)