class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        if len(nums) <= 2:
            return max(0,nums[0],nums[-1])

        dp = [0 for _ in range(len(nums))]
        dp[0] = max(0,nums[0])
        dp[1] = max(dp[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])

        return dp[-1]

a = Solution()
print(a.rob([-2,7,-9,3,1]))