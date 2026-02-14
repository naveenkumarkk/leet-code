from collections import deque
class MinStack:

    def __init__(self):
        self.stack = deque()
        self.stackMin = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.stackMin:
            self.stackMin.append(val)  
        else:
            self.stackMin.append(min(self.stackMin[-1],val))


    def pop(self) -> None:
        self.stack.pop()
        self.stackMin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stackMin[-1]


        
