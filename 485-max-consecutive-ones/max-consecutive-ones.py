class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        maxCounter = 0

        for i in nums:
            if i is 1: counter += 1
            else:counter = 0 
            
            if maxCounter < counter :maxCounter = counter

        return maxCounter