import collections
class Solution:
    def leastBricks(self, wall: [[int]]) -> int:
        d = collections.defaultdict(int)
        for line in wall:
            i = 0
            for brick in line[:-1]:
                i += brick
                d[i] += 1
        # print len(wall), d
        return len(wall) - max(d.values(), default=0)

class BestSolution:
    def leastBricks(self, wall: [[int]]) -> int:
        d = {}
        for w in wall:
            c = 0
            for i in range(len(w)-1):
                c+=w[i]
                if c in d:
                    d[c]+=1
                else:
                    d[c] = 1
        if not d:
            return len(wall)
        m = max(d.values())
        return len(wall)-m

a = Solution()
print(a.leastBricks([[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]))
        