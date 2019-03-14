class Solution {
    public int[] anagramMappings(int[] A, int[] B) {
        int len = A == null ? 0 : A.length;
        int[] result = new int[len];
        if (len == 0 || B == null || len != B.length)
            return result;
        
        Map<Integer, Integer> map = new HashMap<Integer, Integer>(len);
        for(int i = 0; i < len; i++){
            map.put(B[i], i);
        }
        for (int j = 0; j < len; j++){
            result[j] = map.get(A[j]);
        }
        return result;
        
    }
}