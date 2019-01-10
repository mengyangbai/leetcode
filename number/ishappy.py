class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n in [9,8,6,5,4,3,2]:
            return False
        
        if n in [7,1]:
            return True
        
        num = 0
        for ch in str(n):
            num += int(ch)*int(ch)
        
        return self.isHappy(num)


a = Solution()
print(a.isHappy(19))