class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack:
            ans = self.stack[0]
            del self.stack[0]
            return ans
        else:
            return -1

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack:
            return self.stack[0]
        else:
            return -1

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.stack:
            return False
        else:
            return True

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()