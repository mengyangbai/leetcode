class Solution:
    def arrayNesting(self, nums: '[int]') -> 'int':
        res = 0
        length = len(nums)
        seen = [False] * length
        
        def process(i:'int') -> 'int':
            count = 0
            while True:
                seen[i] = True
                i = nums[i]
                count += 1
                if seen[i]:
                    break
            
            return count

        for i in range(length):
            if not seen[i]:
                res = max(process(i),res)
                if res >= length / 2:
                    return res
        

        return res

a = Solution()
print(a.arrayNesting([5,4,0,3,1,6,2]))


