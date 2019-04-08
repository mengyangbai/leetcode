import math
import re

class Solution:
    def fractionAddition(self, expression):
        ints = map(int, re.findall(r'[+-]?\d+', expression))
        A, B = 0, 1
        for a in ints:
            b = next(ints)
            A = A * b + a * B
            B *= b
            g = math.gcd(A, B)
            A //= g
            B //= g
        return '%d/%d' % (A, B)