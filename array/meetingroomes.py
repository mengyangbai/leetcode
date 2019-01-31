# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if not intervals:
            return True
        
        def getKey(interval):
            return interval.start

        intervals.sort(key = getKey)
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        
        return True

a = Solution()
# print(a.canAttendMeetings([[0,30],[5,10],[15,20]]))
print(a.canAttendMeetings([[7,10],[2,4]]))
        