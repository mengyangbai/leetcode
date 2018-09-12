class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        def toNumber(gene):
            table = {v : i for i, v in enumerate('ATGC')}
            return sum([table[g] * 1 << (2 * i) for i, g in enumerate(gene)])

        bank = set(map(toNumber, bank))
        start = toNumber(start)
        end = toNumber(end)
        queue = [(start, 0)]
        viset = set([start])
        while queue:
            gene, step = queue.pop(0)
            if gene == end:
                return step
            for x in range(8):
                for y in range(4):
                    next = gene ^ (y << (x * 2))
                    if next in bank and next not in viset:
                        viset.add(next)
                        queue.append((next, step + 1))
        return -1