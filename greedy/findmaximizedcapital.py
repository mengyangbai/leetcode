import heapq
class Solution:
    def findMaximizedCapital(self, k: 'int', W: 'int', Profits: '[int]', Capital: '[int]') -> 'int':
        heap = []
        projects = sorted(zip(Profits, Capital), key=lambda l: l[1])
        i = 0
        for _ in range(k):
            while i < len(projects) and projects[i][1] <= W:
                heapq.heappush(heap, -projects[i][0])
                i += 1
            if heap: W -= heapq.heappop(heap)
        return W
        
a = Solution()
a.findMaximizedCapital(2,0,[1,2,3],[0,1,1])