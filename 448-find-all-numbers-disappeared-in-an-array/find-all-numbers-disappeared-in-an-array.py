class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arrayLength = len(nums) +1
        countArray = []
        countArray[:arrayLength] = [0] * arrayLength
       
        result = []
        for i in range(arrayLength-1):
            countArray[nums[i]] += 1

        for num in range(1,arrayLength):
            if countArray[num] == 0:
                result.append(num)

        return result
