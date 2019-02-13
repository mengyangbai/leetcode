
class Solution(object):
    def findDuplicate(self, nums):
        slow,fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        
        return fast

nums = [5,1,2,3,4,5]
a = Solution()
print(a.findDuplicate(nums))