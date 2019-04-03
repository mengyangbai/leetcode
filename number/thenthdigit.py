class Solution(object):
    def findNthDigit(self, n):
        start, size = 1, 1
        while n > size:
            n, start = n - size, start + 1
            size = len(str(start))
        return int(str(start)[n-1])


'''
class Solution {
	public int findNthDigit(int n) {
		int len = 1;
		long count = 9;
		int start = 1;

		while (n > len * count) {
			n -= len * count;
			len += 1;
			count *= 10;
			start *= 10;
		}

		start += (n - 1) / len;
		String s = Integer.toString(start);
		return Character.getNumericValue(s.charAt((n - 1) % len));
	}
}
'''