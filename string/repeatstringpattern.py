class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        """
        :type str: str
        :rtype: bool
        """
        if not s:
            return False
            
        ss = (s + s)[1:-1]
        return ss.find(s) != -1

a = Solution()
print(a.repeatedSubstringPattern('abcabcabcabc'))

'''
public boolean repeatedSubstringPattern(String str) {
	int l = str.length();
	for(int i=l/2;i>=1;i--) {
		if(l%i==0) {
			int m = l/i;
			String subS = str.substring(0,i);
			StringBuilder sb = new StringBuilder();
			for(int j=0;j<m;j++) {
				sb.append(subS);
			}
			if(sb.toString().equals(str)) return true;
		}
	}
	return false;
}
'''