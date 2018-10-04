class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = set()
        for n in nums:
            if n in res:
                res.remove(n)
            else:
                res.add(n)
            
        return res.pop()
        