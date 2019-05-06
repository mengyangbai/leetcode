class Solution:
    def maxKilledEnemies(self, grid: [[str]]) -> int:

        if not grid or len(grid[0]) == 0:
            return 0
        
        result = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'E':
                    tmpx = i
                    while tmpx >= 0 and grid[tmpx][j] != 'W':
                        if grid[tmpx][j] != 'E':
                            result[tmpx][j] += 1
                        tmpx -= 1

                    tmpx = i + 1
                    while tmpx < len(grid) and grid[tmpx][j] != 'W':
                        if grid[tmpx][j] != 'E':
                            result[tmpx][j] += 1
                        tmpx += 1

                    tmpy = j
                    while tmpy >= 0 and grid[i][tmpy] != 'W':

                        if grid[i][tmpy] != 'E':
                            result[i][tmpy] += 1
                        tmpy -= 1

                    tmpy = j + 1
                    while tmpy < len(grid[0]) and grid[i][tmpy] != 'W':

                        if grid[i][tmpy] != 'E':
                            result[i][tmpy] += 1
                        tmpy += 1

        return max(map(max, result))

a = Solution()
print(a.maxKilledEnemies([["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]))

class BetterSolution:
    def maxKilledEnemies(self, grid: [[str]]) -> int:
        # intuition
        # dfs until hit wall, but since the bomb never switch row/columns
        # we can use wall as partition
        # for each row/column, create # of E separated by Ws
        # [[2, 3], 
        #  [5, 6]]
        # [[3, 7]
        #  [4, 8,
        #      2]]
        # considering 1D case
        # just do above and picke maximum
        # first build a column query for the maximum kill on that column 
        # then later when you iterate rows, you know how many you can kill on that [i][j] combined
        # but the first building operation takes O(N^2) -> not O(N^2) just O(N) as you will only assign kills once
        m = len(grid)
        if m==0: return 0
        n = len(grid[0])
        kills = [[0]*n for _ in range(m)]
        # build column query -> maximum kills vertically on kills[i][j]
        for j in range(n):
            ne = 0
            p = 0
            for i in range(m):
                if grid[i][j]=='E': ne+=1
                elif grid[i][j]=='W':# need to update previous cells
                    while p<i:
                        if grid[p][j]=='E': 
                            p+=1
                            continue
                        kills[p][j] =ne 
                        p+=1
                    p=i+1
                    ne = 0
            while p<m:
                if grid[p][j]=='E': 
                    p+=1
                    continue
                kills[p][j] = ne
                p+=1
        res = 0
        # iterate horizontally, update 
        for i in range(m):
            ne = 0
            p = 0
            for j in range(n):
                if grid[i][j]=='E': ne+=1
                elif grid[i][j]=='W':# need to update previous cells
                    while p<j:
                        if grid[i][p]=='E': 
                            p+=1
                            continue
                        res = max(res, kills[i][p]+ne)
                        p+=1
                    p=j+1
                    ne = 0
            while p<n:
                if grid[i][p]=='E': 
                    p+=1
                    continue
                res = max(res, kills[i][p]+ne)
                p+=1
        return res