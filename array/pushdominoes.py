'''
    'R......R' => 'RRRRRRRR'
    'R......L' => 'RRRRLLLL' or 'RRRR.LLLL'
    'L......R' => 'L......R'
    'L......L' => 'LLLLLLLL'
'''
class Solution:
    def pushDominoes(self, d):
        """
        :type dominoes: str
        :rtype: str
        """
        d = "L" + d + "R"
        res = []
        l = 0
        for r in range(1, len(d)):
            if d[r] == '.':
                continue
            mid = r - l - 1
            if l:
                res.append(d[l])
            if d[l] == d[r]:
                res.append(d[l] * mid)
            elif d[l] == 'L' and d[r] == 'R':
                res.append('.' * mid)
            else:
                res.append('R' * (mid // 2) + '.' * (mid % 2) + 'L' * (mid // 2))
            l = r
        return "".join(res)