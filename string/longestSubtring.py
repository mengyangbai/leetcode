class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        length = 0
        current = ""
        

        i = 0
        j = 0
        while i < len(s) and j < len(s):
            if s[j] in current:
                while s[j] in current:
                    i = i + 1
                    current = s[i:j]
                j = j + 1
                current = s[i:j]
            else:
                j = j + 1
                current = s[i:j]
            
            if len(current) > length:
                length = len(current)

        return length

a = Solution()
print(a.lengthOfLongestSubstring("pwwkew"))
