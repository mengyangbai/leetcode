class Solution:
    def optimalDivision(self, nums: [int]) -> str:
        
        if not nums:
            return None
        
        res = str(nums[0])

        if len(nums) == 1:
            return res

        if len(nums) == 2:
            return res + "/" + str(nums[1])
        
        res += "/(" + str(nums[1])
    

        for i in range(2,len(nums)):
            res += "/" + str(nums[i])
        
        res += ")"

        return res