class BetterSolution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N==0:
            return 0
        if N==1 or N==2:
            return 1
        ans = [0,1]
        for i in range(2,N+1):
            ans.append(ans[i-1] + ans[i-2])
        return ans[N]

class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N in (0,1):
            return N
        else:
            return self.fib(N-1)+self.fib(N-2)