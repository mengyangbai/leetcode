class Solution:
    def hasPath(self, maze, start, destination):

        Q = [start]
        n = len(maze)
        m = len(maze[0])
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        while Q:
            # Use Q.pop() as DFS or Q.popleft() with deque from collections library for better performance. Kudos to @whglamrock
            i, j = Q.pop(0)
            maze[i][j] = 2

            if i == destination[0] and j == destination[1]:
                return True
            
            for x, y in dirs:
                row = i + x
                col = j + y
                while 0 <= row < n and 0 <= col < m and maze[row][col] != 1:
                    row += x
                    col += y
                row -= x
                col -= y
                if maze[row][col] == 0:
                    Q.append([row, col])
        
        return False

class BetterSolution:
    def hasPath(self, maze: 'List[List[int]]', start: 'List[int]', destination: 'List[int]') -> 'bool':
        visited = [[0] * len(maze[0]) for _ in range(len(maze))]
        
        def dfs(maze,x,y,dest,visited):
            if visited[x][y]:
                return False
            
            if x == dest[0] and y == dest[1]:
                return True
            
            visited[x][y] = True
            r = y + 1
            while r < len(maze[0]) and maze[x][r] == 0:
                r += 1
            if dfs(maze,x,r-1,dest,visited):
                return True
            l = y - 1
            while l >= 0 and maze[x][l] == 0:
                l -= 1
            if dfs(maze,x,l+1,dest,visited):
                return True
            u = x - 1
            while u >= 0 and maze[u][y] == 0:
                u -= 1
            if dfs(maze,u+1,y,dest,visited):
                return True
            d = x + 1
            while d < len(maze) and maze[d][y] == 0:
                d += 1
            if dfs(maze,d-1,y,dest,visited):
                return True
            
            return False
        
        return dfs(maze,start[0],start[1],destination,visited)