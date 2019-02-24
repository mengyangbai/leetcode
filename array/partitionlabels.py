import string
class Solution:
    def partitionLabels(self, S: str) -> [int]:
        res = []
        i = 0
        length = len(S)

        stack = set()
        while i < length:
            stack.add(S[i])

            j = length - 1

            while j >= i:
                if S[j] == S[i]:
                    break
                j -= 1
            
            t = i
            while t < j:
                if S[t] not in stack:
                    stack.add(S[t])
                    m = length - 1
                    while m >= i:
                        if S[m] == S[t]:
                            break
                        m -= 1

                    j = max(m,j)
                
                t += 1
            
            res.append(j-i+1)
            stack.clear()
            i = j+1

        return res

class BestSolution:
    def partitionLabels(self, S: 'str') -> '[int]':
        intervals = []
        for char in string.ascii_lowercase:
            if char in S:
                intervals.append((S.index(char), S.rindex(char)))
        
        intervals.sort()
        
        # 26^2 is fast enough
        out = []
        
        this_start = 0
        this_end = 0
        for start, end in intervals:
            # [start, end]
            if this_end < start:
                out.append(this_end - this_start + 1)
                this_start = start
                this_end = end
            else:
                this_end = max(this_end, end)
            
        out.append(this_end - this_start + 1)
        return out

a = BestSolution()
print(a.partitionLabels("ababcbacadefegdehijhklij"))


            



            