class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        if not rooms:
            return True
        
        visited = [True] + [False] * (len(rooms) - 1)

        toVisitList = rooms[0]

        while toVisitList:
            toVisit = toVisitList.pop()
            if not visited[toVisit]:
                visited[toVisit] = True
                toVisitList.extend(rooms[toVisit])

        return min(visited)
    
a = Solution()
print(a.canVisitAllRooms([[1],[2],[3],[]]))
