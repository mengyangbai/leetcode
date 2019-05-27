class Solution:
    def superpalindromesInRange(self, L, R):

        R = int(R)
        L = int(L)
        
        sqrt_sp = ['11', '22']
        
        for i in sqrt_sp:
            for j in ('0','1','2'):
                sqrt_sp.append(str(i[:len(i)//2])+ j +str(i[len(i)//2:]))
            if int(i) **2 > R:
                break
        sqrt_sp.append(1)
        sqrt_sp.append(2)
        sqrt_sp.append(3)
        
        ans  = 0
				
        for i in sqrt_sp:
            s = int(i)**2
            if L <= s <= R and str(s) == str(s)[::-1]:
                ans +=1
        return ans