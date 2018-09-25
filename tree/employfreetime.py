import itertools
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
class Solution:
    def employeeFreeTime(self, avails):
        avails = list(sorted(itertools.chain(*avails), key=lambda interval: interval.start))
        stack = [avails[0]]
        res = list()
        for cur in avails[1:]:
            top = stack.pop()
            if top.end < cur.start:
                res.append(Interval(top.end, cur.start))
                stack.append(cur)
            else:
                if cur.end <= top.end:
                    stack.append(top)
                else:
                    stack.append(cur)
        return res