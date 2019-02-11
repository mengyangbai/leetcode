import collections
import itertools
class BetterSolution(object):
    def minAreaFreeRect(self, points):
        points = [complex(*z) for z in points]
        seen = collections.defaultdict(list)
        for P, Q in itertools.combinations(points, 2):
            center = (P + Q) / 2
            radius = abs(center - P)
            seen[center, radius].append(P)

        ans = float("inf")
        for (center, radius), candidates in seen.items():
            for P, Q in itertools.combinations(candidates, 2):
                ans = min(ans, abs(P - Q) * abs(P - (2*center - Q)))

        return ans if ans < float("inf") else 0

import math
class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        if not points or len(points) < 4:
            return 0

        def _distance(i,j):
            return math.sqrt((points[i][0] -points[j][0]) ** 2 + (points[i][1] -points[j][1]) ** 2)

        def _validRectangle(i,j,m,n):
            if _distance(i,j) == _distance(m,n) and _distance(i,m) == _distance(j,n) and _distance(i,n) == _distance(j,m):
                return True
            return False
            
        
        def _caculate(i,j,m,n):
            line1  = _distance(i,j)
            line2  = _distance(i,m)
            line3  = _distance(i,n)
            return min(line1*line2,line1*line3,line2*line3)

        res = float('inf')
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                for m in range(j+1,len(points)):
                    for n in range(m+1, len(points)):
                        if _validRectangle(i,j,m,n):
                            res = min(res, _caculate(i,j,m,n))
        
        return round(res,5) if res != float('inf') else 0

a = BetterSolution()
print(a.minAreaFreeRect([[0,1],[2,1],[1,1],[1,0],[2,0]]))