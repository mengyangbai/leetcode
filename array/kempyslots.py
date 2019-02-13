# The idea is to use an array days[] to record each position's flower's 
# blooming day. That means days[i] is the blooming day of the flower in position i+1.
#  We just need to find a subarray days[left, left+1,..., left+k-1, right] which satisfies: 
#  for any i = left+1,..., left+k-1, we can have days[left] < days[i] && days[right] < days[i]. 
#  Then, the result is max(days[left], days[right]).


class Solution:
    def kEmptySlots(self, flowers: '[int]', k: 'int') -> 'int':
        days = [0] * len(flowers)
        for i in range(len(flowers)):
            days[flowers[i]-1] = i + 1
        
        left,right = 0,k+1
        res = float('inf')

        i = 0
        while right < len(days):
            if (days[i]<days[left]) or (days[i] <= days[right]):
                if i==right:
                    res = min(res,max(days[left],days[right]))
                
                left = i
                right = k+1+i
            i += 1
        
        return -1 if res == float('inf') else res

a = Solution()
print(a.kEmptySlots([1,3,2],1))