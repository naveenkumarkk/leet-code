class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = [[p,s] for p,s in zip(position,speed)]
        stack = []
        for position,speed in sorted(car)[::-1]:
            stack.append((target-position)/speed)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()          
        return len(stack)