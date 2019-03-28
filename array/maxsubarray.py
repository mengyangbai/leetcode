class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        max_ending = max_current = nums[0]

        for i in nums[1:]:
            max_ending = max(i, max_ending + i)
            max_current = max(max_current, max_ending)

        return max_current
            