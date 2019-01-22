class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        
        stack = []

        for symbol in s:
            if (symbol == ')' and '(' not in stack) or (symbol == '}' and '{' not in stack) or (symbol == ']' and '[' not in stack):
                return False
            elif symbol in '({[':
                stack.append(symbol)
            else:
                if symbol == ')':
                    if stack[-1] != '(':
                        return False
                    else:
                        stack.pop()
                elif symbol == '}':
                    if stack[-1] != '{':
                        return False
                    else:
                        stack.pop()
                elif symbol == ']':
                    if stack[-1] != '[':
                        return False
                    else:
                        stack.pop()
        
        return True if len(stack) == 0 else False

a = Solution()
print(a.isValid("()"))
print(a.isValid('''()[]{}'''))
print(a.isValid("(]"))
print(a.isValid("([)]"))