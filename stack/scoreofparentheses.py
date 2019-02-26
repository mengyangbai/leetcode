class BestSolution:
    def scoreOfParentheses(self, S: 'str') -> 'int':
        st = [0]
        for ch in S:
            if ch == "(":
                st.append(0)
            else:
                last = st.pop()
                st[-1] += 2*last or 1
        return st.pop()

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for char in S:
            if char == '(':
                stack.append(char)
            
            else:
                if stack[-1] != '(':
                    num = stack.pop()
                    stack.pop()
                    if len(stack) != 0 and stack[-1] != '(':
                        stack[-1] = stack[-1] + num*2
                    else:
                        stack.append(num*2)
                else:
                    stack.pop()
                    if len(stack) != 0 and stack[-1] != '(':
                        stack[-1] = stack[-1] + 1
                    else:                                      
                        stack.append(1)

        return stack[0]

a = BestSolution()

print(a.scoreOfParentheses("(()(()))"))