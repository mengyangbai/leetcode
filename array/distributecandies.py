class BetterSolution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        max_difference = len(candies) / 2
        d = len(set(candies))
        if d > max_difference:
            return max_difference
        else:
            return d

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        count = 0
        countsis = 0
        res = set()
        for e in candies:
            if e not in res:
                countsis+=1
                res.add(e)
            count+=1
        
        return count//2 if countsis > count // 2 else countsis
        

a = Solution()
a.distributeCandies([1,1,2,2,3,3])