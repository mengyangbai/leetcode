class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobodic = {
            '0':'0',
            '1':'1',
            '6':'9',
            '9':'6',
            '8':'8'
        }
        reversedstr = ''
        for ch in reversed(num):
            if ch not in strobodic:
                return False
            
            reversedstr += strobodic[ch]

        return int(num) == int(reversedstr)

a = Solution()
print(a.isStrobogrammatic("69"))
print(a.isStrobogrammatic("88"))
print(a.isStrobogrammatic("962"))
print(a.isStrobogrammatic("880"))
print(a.isStrobogrammatic("000"))