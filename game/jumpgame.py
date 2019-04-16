class Solution:
    def jump(self, nums: [int]) -> int:
        if len(nums) == 1:
            return 0

        steps, limit, next_step = 0,0,0

        for i in range(len(nums)):
            next_step = max(next_step,i+nums[i])

            if i == limit:
                steps+=1
                limit = next_step

                if limit >= len(nums) - 1:
                    return steps

        
        return steps


class BestSolution:
    def jump(self, nums: [int]) -> int:
        length = len(nums)
        target = length-1
        steps, far, i = 0, target, target
        if nums.count(1) == length:  # all 1's = steping
            return length - 1
        while i > 0: # moving cursor from target back to 0
            for j in range(0, i+1):
                # find the farthest one step that can reach target
                # scan until position 0
                if j+nums[j] >= i:
                    far = j  # the first j fulfills this is the farthest
                    break
            steps += 1
            i = far
        return steps