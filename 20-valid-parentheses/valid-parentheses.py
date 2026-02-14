from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        if len(s) %2 != 0:
            return False
        for char in s:
            if char in ["[","{","("]:
                stack.append(char)
            elif char in ["]","}",")"]:
                if len(stack) == 0:
                    return False 
                lastStackEle = stack.pop()
                if char == "]" and lastStackEle == "[":
                    continue
                elif char == ")" and lastStackEle == "(":
                    continue
                elif char == "}" and lastStackEle == "{":
                    continue
                else:
                    return False          

        return len(stack) == 0
        
