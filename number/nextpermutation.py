class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1

        while n >= 0 and nums[n-1] >= nums[n]:
            n-= 1
        
        if n == 0 or n == -1:
            self.reverse(nums,0,len(nums)-1)
        else:
            num = nums[n-1]
            self.reverse(nums, n,len(nums) - 1)
            i = n
            
            while num >= nums[i]:
                i += 1
            
            nums[n-1],nums[i] = nums[i],nums[n-1]

        print(nums)

    def reverse(self,nums,l,r):
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1

        

a = Solution()
b = [3,2,1]

a.nextPermutation(b)

print(b)
