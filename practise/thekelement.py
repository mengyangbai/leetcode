import heapq


class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.heap = []
        self.k = k
        for i in range(len(nums)):
            self.add(nums[i])

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.k == 0:
            if self.heap[0] <= val:
                heapq.heapreplace(self.heap, val)

            return self.heap[0]
        else:
            self.k = self.k - 1
            heapq.heappush(self.heap, val)
            if self.k == 0:
                return self.heap[0]
            else:
                return None


k = 3
arr = [4, 5, 8, 2]
c = KthLargest(k, arr)

c.add(3)
c.add(5)
c.add(10)
