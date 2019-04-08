class Solution:
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        eps = 0.001
        ops = ["+", "-", "*", "/"]
        nums = [float(num) for num in nums]
        
        return self.helper(nums, ops, eps)
    
    
    def helper(self, nums, ops, eps):
        
        if len(nums) == 1:
            return abs(nums[0] - 24) < eps
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                tmp = []
                for k in range(len(nums)):
                    if k != i and k != j:
                        tmp.append(nums[k])
                                
                for op in ops:
                    if (op == "+" or op == "*") and i > j: # avoid repeat calculation of + and *
                        continue
                    if op == "/" and nums[j] < eps: # cannot be divided by 0
                        continue
                    
                    if op == "+":
                        tmp.append(nums[i] + nums[j])
                    elif op == "-":
                        tmp.append(nums[i] - nums[j])
                    elif op == "*":
                        tmp.append(nums[i] * float(nums[j]))
                    elif op == "/":
                        tmp.append(nums[i] / float(nums[j]))
                    
                    if self.helper(tmp, ops, eps):
                        return True
                    tmp.pop()

        return False