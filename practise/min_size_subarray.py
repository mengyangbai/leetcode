class Solution(object):
    def which_to_delete(self,nums,s):
        i, j = 0, len(nums) - 1
        if nums[i]>=s:
            return i
        if nums[j]>s:
            return j
        
        while i<j and nums[i] == nums[j]:
            i+=1
            j-=1
        
        if i > j or nums[i]<nums[j]:
            return 0
        if nums[i]>nums[j]:
            return len(nums) - 1
            
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums)<s:
            return 0
        while sum(nums) >= s:
            i = self.which_to_delete(nums,s)
            del nums[i]
        
        if nums is None:
            return 1

        res = len(nums)+1
        return res
        
a = Solution()
s = 4
b = [1,4,4]
a.minSubArrayLen(s,b)