class Solution(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        N = len(S)
        bold = [0] * (N + 2)
        for word in words:
            start = 0
            while True:
                idx = S[start:].find(word)
                if idx < 0: break
                for x in range(start + idx, start + idx + len(word)):
                    bold[x + 1] = 1
                start += idx + 1
        S = list(S) + ['']
        ans = []
        for x in range(1, N + 1):
            if bold[x] == 1 and bold[x - 1] == 0:
                ans.append('<b>')
            ans.append(S[x - 1])
            if bold[x] == 1 and bold[x + 1] == 0:
                ans.append('</b>')
        return ''.join(ans)