class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in ['+','-','*','/']:
                right = stack.pop()
                left = stack.pop()

                if token == "+":
                    ans = right + left 
                elif token == "-":
                    ans = left - right
                elif token == "*":
                    ans = right * left 
                elif token == "/":
                    ans = int(left/right)
                stack.append(ans)
            else:
                stack.append(int(token))

        return stack[-1]