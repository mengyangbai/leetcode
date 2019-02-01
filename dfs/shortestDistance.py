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
            if point[0] >= 0 and point[0] < len(maze[0]) and point[1]>=0 and point[1] < len(maze) and maze[point[0]][point[1]] == 0:
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

maze = [[0,0,1,0,0],
[0,0,0,0,0],
[0,0,0,1,0],
[1,1,0,1,1],
[0,0,0,0,0]]

a = Solution()
print(a.shortestDistance(maze,[0,4],[4,4]))