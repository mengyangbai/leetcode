import collections
class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return sum([value % 2 for value in collections.Counter(s).values()]) == (len(s) % 2)