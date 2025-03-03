class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
    
        total=0
        init_multiply = 1
        result = []
        if digits[-1] > 8:
            for i in range(len(digits)-1,-1,-1):
                digits[i] *= init_multiply
                print(digits[i])
                init_multiply *=10
                total += digits[i]
            
            total +=1
            total = str(total)
            
            for j in total:
                result.append(int(j))
            
            return result
        else:
            digits[-1] += 1
            return digits