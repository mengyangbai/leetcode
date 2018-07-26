class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dic = {}
        for a in A:
            for b in B:
                if a + b in dic:
                    dic[a + b][0] += 1
                else:
                    dic[a + b] = [1, 0]

        for c in C:
            for d in D:
                if (c + d) * -1 in dic:
                    dic[(c + d) * -1][1] += 1

        res = 0
        for key, v in dic.items():
            res = res + v[0] * v[1]
        return res
