import operator
import functools
class Solution(object):
    def __init__(self):
        self.exprchars = 'abcdefghijklmnopqrstuvwxyz0123456789+-'

    def findGroup(self, expression):
        cnt = 1
        for x in range(1, len(expression)):
            if expression[x] == '(': cnt += 1
            elif expression[x] == ')': cnt -= 1
            if cnt == 0: return expression[:x+1], expression[x+1:]
    
    def findExpr(self, expression):
        for x in range(len(expression)):
            if not expression[x] in self.exprchars:
                return expression[:x], expression[x:]
        return expression, ''

    def solve(self, expression, dmap):
        if expression[0] in '+-' or expression.isdigit(): return int(expression)
        elif expression in dmap: return dmap[expression]
        es = expression[1:-1]
        tokens = []
        while es:
            if es[0] == ' ':
                es = es[1:]
                continue
            elif es[0] in self.exprchars:
                token, es = self.findExpr(es)
            elif es[0] == '(':
                token, es = self.findGroup(es)
            tokens.append(token)
        if tokens[0] == 'add':
            return sum(self.solve(token, dict(dmap)) for token in tokens[1:])
        elif tokens[0] == 'mult':
            return functools.reduce(operator.mul, (self.solve(token,  dict(dmap)) for token in tokens[1:]))
        elif tokens[0] == 'let':
            for x in range(1, len(tokens) - 1, 2):
                dmap[tokens[x]] = self.solve(tokens[x + 1],  dict(dmap))
            return self.solve(tokens[-1],  dict(dmap))

    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        return self.solve(expression, {})