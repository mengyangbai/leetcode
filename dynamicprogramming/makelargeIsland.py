class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h, w = len(grid), len(grid[0])
        mark = [[0] * w for x in range(h)]
        
        def neighbors(x, y):
            for dx, dy in zip((1, 0, -1, 0), (0, 1, 0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and grid[nx][ny]:
                    yield (nx, ny)

        def calcAndMarkArea(sx, sy, mk):
            q = [(sx, sy)]
            vset = set(q)
            ans = 0
            while q:
                x, y = q.pop(0)
                ans += 1
                for nx, ny in neighbors(x, y):
                    if (nx, ny) not in vset:
                        vset.add((nx, ny))
                        q.append((nx, ny))
            for x, y in vset:
                mark[x][y] = mk
                grid[x][y] = ans
            return ans

        maxArea = 0
        mk = 0
        for x in range(h):
            for y in range(w):
                if grid[x][y] and not mark[x][y]:
                    mk += 1
                    maxArea = max(calcAndMarkArea(x, y, mk), maxArea)

        for x in range(h):
            for y in range(w):
                if grid[x][y] == 0:
                    area = 0
                    mkset = set()
                    for nx, ny in neighbors(x, y):
                        if mark[nx][ny] not in mkset:
                            mkset.add(mark[nx][ny])
                            area += grid[nx][ny]
                    maxArea = max(maxArea, area + 1)
        return maxArea
        