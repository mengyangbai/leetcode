class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x:
            return x
        
        checkedStr = str(x)
        if checkedStr[0] == '-':
            checkedStr = checkedStr[::-1]
            i = 0
            while checkedStr[i] == '0':
                i += 1
        
            return int(checkedStr[i:-1]) * -1 if int(checkedStr[i:-1]) * -1 > -2 ** 31 + 1 else 0
        else:
            checkedStr = checkedStr[::-1]
            i = 0
            while checkedStr[i] == '0':
                i += 1
        
            return int(checkedStr[i:]) if int(checkedStr[i:]) < 2 ** 31 -1 else 0

a = Solution()
print(a.reverse(1563847412))