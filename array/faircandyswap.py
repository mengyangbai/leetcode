class Solution:
    def fairCandySwap(self, A: [int], B: [int]) -> [int]:
        a, b = sum(A), sum(B)
        diff = (a-b)//2
        i, j = 0, 0
        A.sort()
        B.sort()
        while i < len(A) and j < len(B):
            temp = A[i]-B[j]
            if temp == diff:
                return [A[i], B[j]]
            elif temp < diff:
                i += 1
            else:
                j += 1


'''
public int[] fairCandySwap(int[] A, int[] B) {
	int sa = 0, sb = 0;
	Set<Integer> S = new HashSet<>();
	for (int n : A) { sa += n; S.add(n); }
	for (int n : B) { sb += n; }
	int d = (sa - sb) / 2;
	for (int n : B) if (S.contains(n + d)) return new int[]{n + d, n};
	return null;
}
'''
