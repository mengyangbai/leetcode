# 利用辅助二维数组mark记录grid中的元素属于哪个岛屿

# 遍历grid，利用BFS标记其中的岛屿，将非0元素替换为其连通区域的大小，并在mark中记录其标号，记录并更新最大值

# 再次遍历grid，尝试将0元素上下左右的岛屿进行加和，记录并更新最大值

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
        