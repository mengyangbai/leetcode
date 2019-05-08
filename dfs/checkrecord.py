class Solution:
    def checkRecord(self, n: int) -> int:
        
        L,P,A_L,A_P,A=[0]*(n+1),[0]*(n+1),[0]*(n+1),[0]*(n+1),[0]*(n+1)
        L[1]=1
        P[1],P[0]=1,1
        A_L[1]=0
        A_P[1]=0
        A[1]=1
        N=10**9 + 7
        for i in range(2,n+1):
            L[i]=(P[i-1]+P[i-2])%N
            P[i]=(P[i-1]+L[i-1])%N
            A_L[i]=(A_P[i-1]+A_P[i-2]+A[i-1]+A[i-2])%N
            A_P[i]=(A_P[i-1]+A_L[i-1]+A[i-1])%N
            A[i]=(L[i-1]+P[i-1])%N                                                         
        return sum([L[-1],P[-1],A_L[-1],A_P[-1],A[-1]])%N