class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = 0
        k = len(nums)
        for i in range(k-n):
            if nums[i]==0:
                while k-1-n >= i or nums[k-1-n]==0:
                    n+=1
                nums[i],nums[k-1-n]=nums[k-1-n],nums[i]

if __name__ == "__main__":
    a = Solution()
    nums = [0]
    a.moveZeroes(nums)