class Solution:
    def canWinNim(self, n: int) -> bool:
        return False if n % 4 == 0 else True

'''
class Solution {
    public boolean canWinNim(int n) {
        return (n % 4 != 0);        
    }
}
'''
