from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        if len(s) %2 != 0:
            return False
        for char in s:
            if char in ["(","[","{"]:
                stack.append(char)
            elif char in [")","]","}"]:
                if len(stack) == 0:
                    return False
                lastChar = stack.pop()
                if char == "]" and lastChar == "[":
                    continue
                elif char == ")" and lastChar == "(":
                    continue
                elif char == "}" and lastChar == "{":
                    continue
                else:
                    return False
                
        return len(stack) == 0
                    
                     
            

