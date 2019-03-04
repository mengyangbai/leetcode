import collections
class Solution:
    def findLongestWord(self, s: str, d: [str]) -> str:
        res = []

        dmap = collections.defaultdict(list)
        for w in d:
            dmap[w[0]].append((0,w))

        for c in s:
            wlist = dmap[c]
            del dmap[c]
            for i,w in wlist:
                if i + 1 == len(w):
                    res.append(w)
                else:
                    dmap[w[i+1]].append((i+1,w))

        if not res: return ''

        maxl = len(max(res,key=len))
        return min(w for w in res if len(w)==maxl)

a = Solution()
a.findLongestWord("abpcplea", ["ale","apple","monkey","plea"])