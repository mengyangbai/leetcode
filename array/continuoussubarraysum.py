class Solution:
    def checkSubarraySum(self, nums: [int], k: int) -> bool:
        
        cur_sum = 0
        cache = {0:-1}
        
        for i in range(len(nums)):
            cur_sum+=nums[i]
            if k!=0:
                cur_sum %= k
            if cur_sum in cache:
                if i - cache[cur_sum] > 1:
                    return True
            else:
                cache[cur_sum] = i
        return False
        