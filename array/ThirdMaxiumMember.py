class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        import heapq
        return heapq.nlargest(3, set(nums))[2 if len(set(nums))>2 else 0]