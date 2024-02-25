# Thought Process
# We need to find the maximum sum of minimum two elements
# We need to sort the array
# sum the of min two elements 
# We can identify the result

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxResult = 0
        for i in range(0,len(nums),2):
            maxResult += min(nums[i] , nums[i+1])
        return maxResult
    
    def bubbleSort(self,nums:List[int]) -> List[int]:
        arrayLength = len(nums)

        for initialIndex in range(arrayLength):
            swapped = False
            for nextIndex in range(arrayLength - initialIndex - 1):
                if nums[nextIndex] > nums[nextIndex+1]:
                    tempElement =  nums[nextIndex]
                    nums[nextIndex] =  nums[nextIndex+1]
                    nums[nextIndex+1] = tempElement
                    swapped = True
            
            if swapped == False:
                break


        return nums




