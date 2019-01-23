import collections
class MySolution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        b1, b0 = 0, 0
        for num in nums:
            b0 = (b0 ^ num) & (~b1)
            b1 = (b1 ^ num) & (~b0)
        return b0

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = collections.Counter(nums)
        for k,v in res.items():
            if v == 1:
                return k

a = MySolution()
print(a.singleNumber([2,2,3,2]))

