import itertools

class Solution:
    def longestPalindrome(self, s: str) -> str:
        lp, lp_len = '', 0
        for start, stop in itertools.combinations(range(len(s)+1), 2):
            ss = s[start:stop]  # substring
            if (len(ss) > lp_len) and (ss == ss[::-1]):
                lp, lp_len = ss, len(ss)
        return lp