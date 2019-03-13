class Solution {
    public double champagneTower(int poured, int query_row, int query_glass) {

        double[] res = new double[101];
        res[0] = poured;
        for(int row=1; row<=query_row; row++)
            for(int i=row; i>=0; i--)
                res[i+1] += res[i] = Math.max(0.0, (res[i]-1)/2);
        return Math.min(res[query_glass], 1.0);
        
    }
    
    public static void main(String[] args){
        Solution solution = new Solution();
        System.out.println(solution.champagneTower(2, 1, 1));
    }
}
