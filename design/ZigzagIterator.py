class ZigzagIterator(object):
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.iter1 = iter(v1)
        self.iter2 = iter(v2)
        self.ind1 = len(v1)
        self.ind2 = len(v2)
        self.flag = True
    
    def next(self):
        """
        :rtype: int
        """
        if self.ind1 > 0 and self.ind2 > 0:
            if self.flag:
                self.flag = False
                self.ind1 -= 1
                return next(self.iter1)
            else:
                self.flag = True
                self.ind2 -= 1
                return next(self.iter2)
        elif self.ind1 > 0:
            self.ind1 -= 1
            return next(self.iter1)
        elif self.ind2 > 0:
            self.ind2 -= 1
            return next(self.iter2)
        else:
            return None
    
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.ind1 > 0 or self.ind2 > 0:
            return True
        else:
            return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
