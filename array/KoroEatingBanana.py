class Solution:
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        # Binary Search
        def isOK(K):  # 判断当前值，是否满足要求
            return sum((p-1)//K + 1 for p in piles) <= H

        low, high = 1, max(piles)  # 初始化上下界

        while low < high:  # 以low ，high 为上下界，开始二分搜索
            mid = (low + high) // 2
            if not isOK(mid):
                low = mid + 1
            else:
                high = mid
        return low