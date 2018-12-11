class Solution:
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        size = len(word)
        cnt = loc = 0
        for w in abbr:
            if w.isdigit():
                if w == '0' and cnt == 0:
                    return False
                cnt = cnt * 10 + int(w)
            else:
                loc += cnt
                cnt = 0
                if loc >= size or word[loc] != w:
                    return False
                loc += 1
        return loc + cnt == size
        