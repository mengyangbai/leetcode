class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1

        frequent = [[] for x in range(n + 1)]

        for key in dic:
            frequent[dic[key]].append(key)

        res = []
        for p in range(n, 0, -1):
            res.extend(frequent[p])

        return res[:k]
