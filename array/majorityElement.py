class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        dic = {}
        ls = len(nums)
        for x in nums:
            if x not in dic:
                dic[x] = 1
            else:
                dic[x] += 1
            if dic[x] >= ls // 3 + 1 and x not in res:
                res.append(x)
        return res

class MySolution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        n = len(nums) // 3
        dic = {}
        res = []
        for num in nums:
            if num in dic and num not in res:
                dic[num] += 1
            else:
                dic[num] = 1
            
            if dic[num] > n and num not in res:
                res.append(num)
        
        return res

a = Solution()
print(a.majorityElement([2,2]))
