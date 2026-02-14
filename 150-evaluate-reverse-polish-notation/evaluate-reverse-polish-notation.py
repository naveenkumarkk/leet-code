from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operator = ''

        for ele in tokens:
            if ele not in ['+','-','*','/']:
                stack.append(int(ele))
            else:
                right = stack.pop()
                left = stack.pop()
                if ele == '+':
                    res = right + left
                elif ele == '-':
                    res = left - right
                elif ele == '*':
                    res = right * left
                elif ele == '/':
                    res = int(left/right)
                stack.append(res)
        return stack[-1]

                

        
        