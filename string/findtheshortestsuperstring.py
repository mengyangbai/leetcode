class Solution:
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        n=len(A)
        adj=[[0 for _ in range(n)] for _ in range(n)]
        
        def helper(s1,s2):
            ma=min(len(s1),len(s2))
            for k in range(ma,0,-1):
                if s1[len(s1)-k:]==s2[:k]: return k
            return 0
            
        for i in range(n):
            for j in range(n):
                if i==j: continue
                adj[i][j]=helper(A[i],A[j])
        
        dp=[[-1 for _ in range(n)] for _ in range(2**n)]
        path=[[-1 for _ in range(n)] for _ in range(2**n)]
        for mask in range(2**n):
            for bit in range(n):
                if mask&(1<<bit):
                    mask2 = mask^(1<<bit)
                    if mask2==0: 
                        dp[mask][bit]=0
                        continue
                    for i in range(n):
                        if mask2&(1<<i):
                            t = dp[mask2][i]+adj[i][bit]
                            if t>dp[mask][bit]:
                                dp[mask][bit] = t
                                path[mask][bit]=i
        mask = 2**n-1
        s = dp[mask].index(max(dp[mask]))
        res=[]
        while len(res)<n:
            res.append(s)
            s = path[mask][s]
            mask = mask^(1<<res[-1])
        res=res[::-1]
        
        s = A[res[0]]
        for i in range(1,n):
            s+=A[res[i]][adj[res[i-1]][res[i]]:]
        return s