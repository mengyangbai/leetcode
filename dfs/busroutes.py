import collections
class Solution(object): 
    def numBusesToDestination(self, routes, S, T): 
        """ 
        :type routes: List[List[int]] 
        :type S: int 
        :type T: int 
        :rtype: int 
        """ 
        busNexts = collections.defaultdict(set)
        stopBuses = collections.defaultdict(set)
        for bus, stops in enumerate(routes):
            for stop in stops: 
                stopBuses[stop].add(bus) 
            
        for buses in stopBuses.values(): 
            for bus in buses: 
                busNexts[bus] |= set(buses) 
                
        q = stopBuses[S] 
        vset = set(q) 
        ans = 0 
        found = False 
        while q and not found: 
            q0 = [] 
            for s in q: 
                if s in stopBuses[T]: 
                    found = True 
                    break 
                for n in busNexts[s]: 
                    if n not in vset: 
                        q0.append(n) 
                        vset.add(n) 
            q = q0 
            ans += 1 
        
        return 0 if S == T else ans if found else -1 


a = Solution()
print(a.numBusesToDestination([[1,2,7],[3,6,7]],1,6))
