class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        ans = duration * len(timeSeries)
        for i in range(1,len(timeSeries)):
            ans -= max(0, duration - (timeSeries[i] - timeSeries[i-1]))
        return ans

class BetterSolution:
    def findPoisonedDuration(self, timeSeries: [int], duration: int) -> int:
        
        time = 0
        
        last = 0
        for i in timeSeries:
            if i > last:
                time += duration
            else:
                time += duration - (last - i)
            last = i+duration
        return time