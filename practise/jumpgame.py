class Solution(object):
    def canJump(self, nums):
        step = nums[0]
        for i in range(1, len(nums)):
            if step > 0:
                step -= 1
                step = max(step, nums[i])
            else:
                return False
        return True


a = Solution()
a.canJump([2, 3, 1, 1, 4])
