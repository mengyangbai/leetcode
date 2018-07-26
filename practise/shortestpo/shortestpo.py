class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        rev_s = s[::-1]
        tmp = s + '#' + rev_s
        p = [0] * len(tmp)
        for i in range(1, len(tmp)):
            j = p[i - 1]
            while j > 0 and tmp[i] != tmp[j]:
                j = p[j - 1]
            p[i] = j + (tmp[i] == tmp[j])
        return rev_s[:len(s) - tmp[-1]] + s


a = Solution()
a.shortestPalindrome("aacecaaa")
