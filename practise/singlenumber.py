class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = set()
        for num in nums:
            if num in res:
                res.remove(num)
            else:
                res.add(num)

        return res.pop()


a = Solution()
a.singleNumber([4, 1, 2, 1, 2])
