class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vset = set([0])
        for c in s:
            nset = set()
            if c == '*':
                for v in vset:
                    nset.add(v + 1)
                    nset.add(v)
                    if v >= 1: nset.add(v - 1)
            elif c == '(':
                for v in vset:
                    nset.add(v + 1)
            elif c == ')':
                for v in vset:
                    if v >= 1: nset.add(v - 1)
            vset = nset
        return 0 in vset