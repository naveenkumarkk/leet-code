class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for key,value in enumerate(temperatures):
            while stack and stack[-1][0] < value:
                temp,stackKey = stack.pop()
                res[stackKey] = key - stackKey
            stack.append([value,key])
        return res