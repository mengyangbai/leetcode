class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        s = set(wordlist)
        trie = dict()
        res = []
        
        # build trie
        for i in range(len(wordlist))[::-1]:
            w = wordlist[i]
            cur = trie
            for c in w:
                if c not in cur:
                    cur[c] = dict()
                cur = cur[c]
            cur['#'] = [i, w]
        
        for q in queries:
            # bfs
            que = [[0, trie]]
            for c in q:
                nex = []
                for order, node in que:
                    if c in node:
                        nex.append([max(0, order), node[c]])
                    if 'a' <= c <= 'z' and c.upper() in node:
                        nex.append([max(1, order), node[c.upper()]])
                    if 'A' <= c <= 'Z' and c.lower() in node:
                        nex.append([max(1, order), node[c.lower()]])
                    if c in 'aeiouAEIOU':
                        for vowel in 'aeiouAEIOU':
                            if vowel != c and vowel in node:
                                nex.append([max(2, order), node[vowel]])
                que = nex
            
            if que:
                order, index, w = sorted([[order, dic['#'][0], dic['#'][1]] for order, dic in que])[0]
                res.append(w)
            else:
                res.append("")
        
        return res
                

class BetterSolution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        d = dict()
        d1 = dict()
        for w in wordlist:
            t = ""
            for c in w.lower():
                if c in "aeiou":
                    t += "a"
                else:
                    t += c
            if t not in d:
                d[t] = [w]
            else:
                d[t].append(w)
            if w.lower() not in d1:
                d1[w.lower()] = [w]
            else:
                d1[w.lower()].append(w)
                
        # print(d)
        output = []

        for q in queries:
            
            if q.lower() in d1:
                if q in d1[q.lower()]:
                    output.append(q)
                else:
                    output.append(d1[q.lower()][0])
                
            else:
                t = ""
                for c in q.lower():
                    if c in "aeiou":
                        t += "a"
                    else:
                        t += c
                if t in d:
                    output.append(d[t][0])
                else:
                    output.append("")

        return output