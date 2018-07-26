class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        dic = {}

        for i in range(len(s)):
            if s[i] in dic:
                if t[i] != dic[s[i]]:
                    return False
            elif t[i] in dic:
                return False
            else:
                dic[s[i]] = t[i]
        return True


a = Solution()
a.isIsomorphic("ab", "aa")
