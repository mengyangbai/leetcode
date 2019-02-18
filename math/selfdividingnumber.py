class Solution:
    def selfDividingNumbers(self, left: 'int', right: 'int') -> '[int]':
        list = []
        for i in range(left, right + 1):
            a = 0
            if '0' not in str(i):
                for j in str(i):
                    if i % int(j) == 0:
                        a += 1
                    if a == len(str(i)):
                        list.append(i)

        return list