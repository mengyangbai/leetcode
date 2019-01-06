class Solution(object):
    def isPalindrome(self, x):
        return x >= 0 and x == int(str(x)[::-1])