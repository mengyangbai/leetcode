class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        514ms
        """
        subsets_A = set()
        subsets_B = set()
        used = set()
        for i in range(len(graph)):
            if i not in used:
                subsets_A.add(i)
                cur_list = [i]
                count = 0
                while cur_list:
                    next_list = []
                    for j in cur_list:
                        used.add(j)
                        for opposite in graph[j]:
                            if count % 2 == 0:
                                if opposite in subsets_A:
                                    return False
                                subsets_B.add(opposite)
                            else:
                                if opposite in subsets_B:
                                    return False
                                subsets_A.add(opposite)
                            if opposite not in used:
                                next_list.append(opposite)
                    count += 1
                    cur_list = next_list
        return True