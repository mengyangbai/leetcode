import math
import bisect
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lst = []
        self.size = 0
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        bisect.insort(self.lst,num)
        self.size += 1
        

    def findMedian(self):
        """
        :rtype: float
        """
        if self.size % 2 == 0:
            i = self.size // 2
            return (self.lst[i] + self.lst[i-1]) / float(2)
        i = int(math.floor(self.size/2))
        return float(self.lst[i])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
a = MedianFinder()
a.addNum(1)
a.addNum(2)
print(a.findMedian())
a.addNum(3)
print(a.findMedian())