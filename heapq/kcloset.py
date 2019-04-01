import heapq
class Solution:
    def kClosest(self, points: [[int]], K: int) -> [[int]]:
        return heapq.nsmallest(K,points,key=lambda K: K[0]**2 + K[1]**2) 
    
        


class MySolution:
    def kClosest(self, points: [[int]], K: int) -> [[int]]:

        points.sort(key = lambda K: K[0]**2 + K[1]**2) 
    
        return points[:K] 


a = Solution()
print(a.kClosest([[1,3],[-2,-2]],1))