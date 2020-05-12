class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.my_stack = []
        self.help_stack = []

    def push(self, x: int) -> None:
        self.my_stack.append(x)
        if not self.help_stack or x < self.help_stack[-1]:
            self.help_stack.append(x)
        else:
            self.help_stack.append(self.help_stack[-1])

    def pop(self) -> None:
        if self.my_stack:
            self.my_stack.pop()
            self.help_stack.pop()

    def top(self) -> int:
        if self.my_stack:
            return self.my_stack[-1]

    def getMin(self) -> int:
        if self.my_stack:
            return self.help_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
