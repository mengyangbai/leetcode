import heapq
class BestSolution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        dest=tuple(destination)
        m=len(maze)
        n=len(maze[0])
        def go(start, direction):
            # return the stop position and length
            i, j = start
            ii, jj = direction
            l=0
            while 0<=i+ii<m and 0<=j+jj<n and maze[i+ii][j+jj]!=1:
                i+=ii
                j+=jj
                l+=1
            return l, (i,j)
        # bfs (dijkstra: https://en.wikipedia.org/wiki/Dijkstra's_algorithm)
        visited={}
        q=[]
        heapq.heappush(q, (0, tuple(start)))
        while q:
            length, cur = heapq.heappop(q)
            if cur in visited and visited[cur]<=length:
                continue # if cur is visited and with a shorter length, skip it.
            visited[cur]=length
            if cur == dest:
                return length
            for direction in [(-1, 0), (1, 0), (0,-1), (0,1)]:
                l, np = go(cur, direction)
                heapq.heappush(q, (length+l, np))
        return -1


class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        
        dp = [[999999 for _ in range(len(maze[0]))] for _ in range(len(maze))]

        dp[start[0]][start[1]] = 0

        directions = [[1,0],[0,1],[-1,0],[0,-1]]


        def inBorder(point):
            if point[0] >= 0 and point[0] < len(maze) and point[1]>=0 and point[1] < len(maze[0]) and maze[point[0]][point[1]] == 0:
                return True
            else:
                return False

        def add(point1,point2):
            return [point1[0]+point2[0],point1[1]+point2[1]]

        def minus(point1,point2):
            return [point1[0]-point2[0],point1[1]-point2[1]]

        def dfs(start):
            for x in directions:
                if inBorder(add(start,x)):
                    count = 0
                    tmp = start
                    while inBorder(tmp):
                        count += 1
                        tmp = add(tmp,x)
                    
                    tmp = minus(tmp,x)
                    count -= 1
                    if dp[start[0]][start[1]] + count < dp[tmp[0]][tmp[1]]:
                        dp[tmp[0]][tmp[1]] = dp[start[0]][start[1]] + count
                        if tmp == destination:
                            continue
                        dfs(tmp)
                

        
        dfs(start)
        
        return dp[destination[0]][destination[1]] if dp[destination[0]][destination[1]] != 999999 else -1

maze = [[0,0,0,0,1,0,0],
[0,0,1,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,1],
[0,1,0,0,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,1,0,0,0,1],
[0,0,0,0,1,0,0]]

a = Solution()
print(a.shortestDistance(maze,[0,0],[8,6]))