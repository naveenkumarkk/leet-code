class Solution:
    def numberOfSteps(self, num: int) -> int:

        result = []
        steps = 0
        i = num
        while num > 0:
            if num%2 == 0:
                num = num/2
            else:
                num = num-1
            steps+=1
    
        return steps
        