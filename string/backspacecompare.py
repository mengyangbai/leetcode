class Solution:    
    def backspaceCompare(self, S, T):
        def check(S):
            res = []
            for ch in S:
                if ch != '#':
                    res.append(ch)
                elif res:
                    res.pop()
            
            return res
        
        return check(S) == check(T)