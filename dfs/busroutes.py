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


class MySolution(object):
    '''
    TLE
    ''' 
    def numBusesToDestination(self, routes, S, T): 
        """ 
        :type routes: List[List[int]] 
        :type S: int 
        :type T: int 
        :rtype: int 
        """ 
        res = []

        def dfs(routes,S,T,path=[]):
            path=path+[S]
            for route in routes:
                if S in route and T in route:
                    path=path+[T]
                    res.append(path)
                    return
                elif S in route and T not in route:
                    for anostation in route:
                        if anostation not in path:
                            dfs(routes,anostation,T,path)

        dfs(routes,S,T)

        if len(res) == 0:
            return -1
        else:
            return min(len(route) for route in res) - 1
a = Solution()
print(a.numBusesToDestination([[25,33],[3,5,13,22,23,29,37,45,49],[15,16,41,47],[5,11,17,23,33],[10,11,12,29,30,39,45],[2,5,23,24,33],[1,2,9,19,20,21,23,32,34,44],[7,18,23,24],[1,2,7,27,36,44],[7,14,33]],
7,
47))
