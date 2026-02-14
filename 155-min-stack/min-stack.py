from collections import deque
class MinStack:

    def __init__(self):
        self.stack = deque()
        self.stackMin = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.stackMin = min(self.stackMin,val)      

    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack) != 0:
            self.stackMin = min(self.stack)
        else:
            self.stackMin = float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stackMin


        
