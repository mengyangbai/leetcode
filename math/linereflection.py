class Solution:

    def isReflected(self, points):

        if (not points):
            return True

        dic = {}
        sumx = 0
        lenwithoutdup = 0
        for point in points:
            if point[1] not in dic:
                dic[point[1]] = {point[0]}
                sumx += point[0]
                lenwithoutdup += 1
            else:
                if point[0] not in dic[point[1]]:
                    dic[point[1]].add(point[0])
                    sumx += point[0]
                    lenwithoutdup += 1

        #print sumx, lenwithoutdup
        avgx = float(sumx)/lenwithoutdup
        for item in dic:
            lst = list(dic[item])
            lst.sort()
            i, j = 0, len(lst)-1  # two pointers
            while i <= j:
                #print lst[i], avgx, lst[j]
                if lst[i] - avgx != avgx - lst[j]:
                    return False
                i += 1
                j -= 1

        return True


class betterSolution:
    def isReflected(self, points: [[int]]) -> bool:
        if not points:
            return True
        midx = (min(x for x, _ in points) + max(x for x, _ in points))/2
        p = set(map(tuple, points))
        return all((2 * midx-x, y) in p for x, y in points)

