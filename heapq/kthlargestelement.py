import heapq
class KthLargest:

    def __init__(self, k: 'int', nums: '[int]'):
        self.heap = []
        self.k = k
        for i in range(len(nums)):
            self.add(nums[i])

    def add(self, val: 'int') -> 'int':
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


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

k = 3
arr = [4,5,8,2]
kthLargest = KthLargest(3, arr)
print(kthLargest.add(3))
print(kthLargest.add(5))
print(kthLargest.add(10))
print(kthLargest.add(9))
print(kthLargest.add(4))