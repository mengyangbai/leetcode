import itertools
class Solution:
    def largestTimeFromDigits(self, A: [int]) -> str:
        h = m = -float("inf")
        for n1, n2, n3, n4 in itertools.permutations(A):
            hh, mm = n1 * 10 + n2, n3 * 10 + n4
            if 0 <= hh <= 23 and 0 <= mm <= 59 and (hh > h or hh == h and mm > m):
                h, m = hh, mm
        sh = str(h) if h > 9 else "0" + str(h)
        sm = str(m) if m > 9 else "0" + str(m)
        return 0 <= h <= 23 and 0 <= m <= 59 and sh + ":" + sm or ""
        
'''
class Solution {

    public String largestTimeFromDigits(int[] A) {       
        Arrays.sort(A);       
               
        String r = "";
        
        for(int i=3;i>=0;i--) {
            for(int j=3;j>=0;j--) {
                if(j==i) continue;
                for(int k=3;k>=0;k--){
                    if(k==j || k==i)  continue;
                    for(int s=3;s>=0;s--){
                        if(s==k||s==j||s==i) continue;
                        String t = time(A[i],A[j],A[k],A[s]);
                        if(!t.equals("")) {
                            return t;
                        }                        
                    }
                }
            }
        }

        return r;       
    }
    
    private String time(int a, int b, int c, int d) { 
        if(a>2||c>5)  return "";
        if(a==2&&b>3) return "";
        
        StringBuilder r = new StringBuilder();
        
        r.append(a);
        r.append(b);
        r.append(":");
        r.append(c);
        r.append(d);
        
        return r.toString();
    }
}
'''