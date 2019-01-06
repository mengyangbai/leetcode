class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        stack = []
        expr = list(expression)
        while len(stack) > 1 or expr:
            tail = stack[-5:]
            if len(tail) == 5 and tail[3] == '?' and tail[1] == ':':
                tail = tail[2] if tail[4] == 'T' else tail[0]
                stack = stack[:-5] + [tail]
            else:
                stack.append(expr.pop())
        return stack[0] if stack else None