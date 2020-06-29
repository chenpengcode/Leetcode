class CQueue:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def appendTail(self, value: int) -> None:
        self.stack_1.append(value)

    def deleteHead(self) -> int:
        if self.stack_2:
            return self.stack_2.pop()
        if self.stack_1:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
            return self.stack_2.pop()
        return -1

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
