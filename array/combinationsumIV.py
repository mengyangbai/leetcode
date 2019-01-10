'''
    TLE
'''
# class Solution:
#     def combinationSum4(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         if not nums:
#             return 0

#         self.n = 0

#         def helper(nums,target):
#             if target == 0:
#                 self.n = self.n + 1
            
#             if target < 0:
#                 return
            
#             if target > 0:
#                 for num in nums:
#                     helper(nums,target-num)
            
        
#         helper(nums,target)

#         return self.n

'''
    AC
''' 
class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0

        dp = [0] * (target + 1)

        for i in range(1,target+1):
            for num in nums:
                if i - num < 0:
                    pass
                if i - num == 0:
                    dp[i] += 1
                if i - num > 0:
                    dp[i] += dp[i - num]

        return dp[target]