class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        n = 0
        m = len(s) - 1

        while n < m:
            if not s[n].isalnum():
                n += 1
            elif not s[m].isalnum():
                m -= 1
            elif s[n].lower() != s[m].lower():
                return False
            else:
                n += 1
                m -= 1

        return True


a = Solution()
print(a.isPalindrome('A man, a plan, a canal: Panama'))
