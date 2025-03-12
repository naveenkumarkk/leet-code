class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        first_pointer, second_pointer = 0,len(numbers)-1
        listLen = len(numbers)
        res = []
        tempSum = 0
        while  first_pointer < second_pointer :
            tempsum = numbers[first_pointer] + numbers[second_pointer]
            if tempsum == target:
                return [first_pointer +1,second_pointer+1]
            elif tempsum < target:
                first_pointer +=1
            else :
                second_pointer -= 1

        return []