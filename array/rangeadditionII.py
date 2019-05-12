class Solution:
    def maxCount(self, m: int, n: int, ops: [[int]]) -> int:
        if not ops:
            return m*n
        return min(op[0] for op in ops)*min(op[1] for op in ops)

'''
public class Solution {
    public int maxCount(int m, int n, int[][] ops) {
        if (ops == null || ops.length == 0) {
            return m * n;
        }
        
        int row = Integer.MAX_VALUE, col = Integer.MAX_VALUE;
        for(int[] op : ops) {
            row = Math.min(row, op[0]);
            col = Math.min(col, op[1]);
        }
        
        return row * col;
    }
}
'''