class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        counter = 0
        for i in nums:
            tempArray = []
            tempArray += str(i)
            tempArrayCount = len(tempArray)
            if tempArrayCount % 2 is 0: counter+=1

        
        return counter
