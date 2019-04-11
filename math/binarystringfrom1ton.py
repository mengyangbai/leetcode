class Solution:
    def queryString(self, S: str, N: int) -> bool:
        i = N
        while i>=N//2 and i >= 1:
            tmp = str(bin(i))[2:]
            if tmp not in S:
                return False
            i -= 1

        return True

a = Solution()
a.queryString('1',1)

'''
class Solution {
    public boolean queryString(String S, int N) {
        int i = N;
        while(i >= N/2 and i >= 1){
            String sub = Integer.toString(i, 2);
            if(!S.contains(sub)) return false;
            i--;
        }
        return true;
    }
}
'''