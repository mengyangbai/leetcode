class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        ts = [[50000, 0]]
        for price in prices:
            if not ts[-1][1] and price <= ts[-1][0]:
                ts[-1][0] = price
            elif price >= max(ts[-1][1], ts[-1][0] + fee):
                ts[-1][1] = price
            elif ts[-1][1]:
                ts.append([price, 0])
            while len(ts) > 1 and ts[-2][1] < ts[-1][0] + fee:
                ts[-1][1] = max(ts.pop()[1], ts[-1][1])
        return sum(t[1] - t[0] - fee for t in ts if t[1] - t[0] > fee)