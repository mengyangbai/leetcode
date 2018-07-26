class Solution(object):
    def helper(self, arr, small, big):
        # left upper = right upper
        lu = ru = small
        ld = rd = big
        for i in range(big - small):
            arr[small][lu], arr[ru][big], arr[big][rd], arr[ld][small] = arr[
                ld][small], arr[small][lu], arr[ru][big], arr[big][rd]
            lu += 1
            ru += 1
            ld -= 1
            rd -= 1

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return

        small = 0
        big = len(matrix) - 1

        while small < big:
            self.helper(matrix, small, big)
            small += 1
            big -= 1
