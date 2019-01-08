
def firstMissingNumber(stack):
    for i in range(0,len(stack)):
        if i not in stack:
            return i
    
    return len(stack)

class Solution:

    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        curlen = 0
        maxlen = 0
        for e,v in enumerate(s):
            if v == '+':
                curlen += 1

            if (e + 1) == len(s) or v == '-':
                if curlen >= 2:
                    stack.append(curlen)
                maxlen = max(maxlen,curlen)
                curlen = 0

        dp = [0] * (maxlen + 1)
        for i in range(2,maxlen+1):
            tmpstack = []
            for len_first_game in range(0,i//2):
                len_second_game = i - len_first_game - 2
                tmpstack.append(dp[len_first_game]^dp[len_second_game])

            dp[i] = firstMissingNumber(tmpstack)

        g_final = 0

        for tmps in stack:
            g_final ^= dp[tmps]
        print(g_final)
        return g_final != 0

            




a = Solution()
a.canWin("+++++++++")
