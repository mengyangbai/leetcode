
class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        moves, n, s = [], len(s), list(s)
        for i in range(n - 1):
            if s[i] == s[i + 1] == '+':
                s[i] = s[i + 1] = '-'
                moves += ''.join(s),
                s[i] = s[i + 1] = '+' 
        return moves