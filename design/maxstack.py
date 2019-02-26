class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop(0)

    def top(self) -> int:
        return self.stack[0]


    def peekMax(self) -> int:
        return max(self.stack)

    def popMax(self) -> int:
        return self.stack.pop(self.stack.index(max(self.stack)))
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
stack = MaxStack()
stack.push(5) 
stack.push(1)
stack.push(5)
stack.top()
stack.popMax()
stack.top()
stack.peekMax()
stack.pop()
stack.top()