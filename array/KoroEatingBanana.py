class Solution:
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        # Binary Search
        def isOK(K):  
            return sum((p-1)//K + 1 for p in piles) <= H

        low, high = 1, max(piles)  

        while low < high: 
            mid = (low + high) // 2
            if not isOK(mid):
                low = mid + 1
            else:
                high = mid
        return low