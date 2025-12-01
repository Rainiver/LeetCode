from collections import deque
class MyStack:
    """
    每次 push 一个新元素进去（肯定在队尾），然后把前面的所有老元素一个接一个取出来，
    再重新 append 到队尾。这样，那个新元素就“转”到了队头。
    """
    def __init__(self):
        self.stack = deque()  

    def push(self, x: int) -> None:
        self.stack.append(x)
        n = len(self.stack)
        for i in range(n-1):
            item = self.stack.popleft()
            self.stack.append(item)
        

    def pop(self) -> int:
        return self.stack.popleft()

    def top(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return True if not self.stack else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()