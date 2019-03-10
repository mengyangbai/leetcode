
from functools import lru_cache
class ExcelSolution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger*(maxChoosableInteger+1)//2 < desiredTotal: return False
        
        @lru_cache(maxsize=None)
        def can_win(selected,current):
            if maxChoosableInteger + current >= desiredTotal:
                    return True
            for n in reversed(range(1,maxChoosableInteger)):
                t = 1<<n
                if t & selected: continue
                choice = selected|t
                if not can_win(choice,current+n): return True
                    
            return False

        
        
        return can_win(0,0)

class Solution(object):
    def helper(self, allowed, target, so_far, cache):
        if len(allowed) == 0:
            return False
        state = tuple(allowed)
        if state in cache:
            return cache[state]
        else:
            cache[state] = False
            if max(allowed) + so_far >= target:
                cache[state] = True
            else:
                for x in allowed:
                    new_allowed = [y for y in allowed if x!=y]
                    if self.helper(new_allowed, target, so_far+x, cache) ==  False:
                        cache[state] = True
                        break
            return cache[state]
    
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        allowed = [x for x in range(1, maxChoosableInteger+1)]
        if sum(allowed) < desiredTotal:
            return False
        return self.helper(allowed, desiredTotal, 0, {})