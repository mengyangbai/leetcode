class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        if A >= 2*B:
            return 'aab'* B + 'a'* (A-2*B)
        elif A >= B:
            return 'aab' * (A-B) + 'ab' * (2*B - A)
        elif B >= 2*A:
            return 'bba' * A + 'b' *(B-2*A)
        else:
            return 'bba' * (B-A) + 'ab' * (2*A - B)

'''
class Solution {
    public String strWithout3a3b(int A, int B) {
      StringBuilder res = new StringBuilder(A + B);
      char a = 'a', b = 'b';
      int i = A, j = B;
      if (B > A) { a = 'b'; b = 'a'; i = B; j = A; }
      while (i-- > 0) {
        res.append(a);
        if (i > j) { res.append(a); --i; }
        if (j-- > 0) res.append(b);
      }
        return res.toString();
    }
}
'''