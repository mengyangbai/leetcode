class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """

        if not costs:
            return 0

        res = [costs[0][0],costs[0][1],costs[0][2]]

        for i in range(1,len(costs)):
            res[0],res[1],res[2] = min(res[1],res[2]) + costs[i][0], min(res[0],res[2]) + costs[i][1], min(res[0],res[1]) + costs[i][2]

        return min(res)

a = Solution()
print(a.minCost([[17,2,17],[16,16,5],[14,3,19]]))