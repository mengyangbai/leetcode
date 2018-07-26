class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        wcount = len(sentence)
        wordlenmap = []
        for singlestr in sentence:
            wordlenmap.append(len(singlestr))
        # wordlenmap = map(len, sentence)
        slen = sum(wordlenmap) + wcount
        dp = dict()
        pr = pc = pw = ans = 0
        while pr < rows:
            if (pc, pw) in dp:
                pr0, ans0 = dp[(pc, pw)]
                loop = (rows - pr0) / (pr - pr0 + 1)
                ans = ans0 + loop * (ans - ans0)
                pr = pr0 + loop * (pr - pr0)
            else:
                dp[(pc, pw)] = pr, ans
            scount = (cols - pc) / slen
            ans += scount
            pc += scount * slen + wordlenmap[pw]
            if pc <= cols:
                pw += 1
                pc += 1
                if pw == wcount:
                    pw = 0
                    ans += 1
            if pc >= cols:
                pc = 0
                pr += 1
        return ans
