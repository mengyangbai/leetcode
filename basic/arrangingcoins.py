
import math
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        #int is simply to floor the floating point so we get the largest integer smaller than the expression
        return int((math.sqrt(8 * n + 1)-1)/2)