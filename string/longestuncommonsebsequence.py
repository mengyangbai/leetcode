class Solution:
    def findLUSlength(self, A: str, B: str) -> int:
        if A == B:
            return -1
        return max(len(A), len(B))

'''
public int findLUSlength(String a, String b) {
    return a.equals(b) ? -1 : Math.max(a.length(), b.length());
}
'''