class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1

        for s in t:
            if s in dic:
                if dic[s] == 1:
                    del dic[s]
                else:
                    dic[s] -= 1
            else:
                return False

        if not dic:
            return True

        return False


a = Solution()
a.isAnagram('', '')
