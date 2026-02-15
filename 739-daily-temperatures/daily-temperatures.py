from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # res = []
        # for i in range(len(temperatures)):
        #     for j in range(i,len(temperatures)):
        #         if temperatures[i] < temperatures[j]:
        #             res.append(j-i)
        #             break
        #         elif j == len(temperatures) - 1:
        #             res.append(0)
        # return res
        
        res = [0] * len(temperatures)
        stack = []

        for key,value in enumerate(temperatures):
            while stack and stack[-1][0] < value:
                temp,stackKey = stack.pop()
                res[stackKey] = key - stackKey
            stack.append([value,key])

        return res