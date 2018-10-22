class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        minval=100000
        nums.sort()
        for i in range(len(nums)):
            #if i>0 and num[i]==num[i-1]:
             #   continue
            left=i+1
            right=len(nums)-1
            while left<right:
                val=nums[i]+nums[left]+nums[right]
                
                if abs(val-target)<minval:
                    minval=abs(val-target)
                    result=val
                if val==target:
                    return target
                if val<=target:
                    left+=1
                else:
                    right-=1
        return result
                    
        