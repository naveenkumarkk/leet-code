class Solution:
    # thought process - since need to check if the largest number is atleast twice as the other elements
    # we need to find the first two largest element
    # if we can calculate the square for second largest and compare it with the largest element, we achieve the desired result
    # Given largest element is unique, so it makes things simple

    def dominantIndex(self, nums: List[int]) -> int:
        copyArray = nums.copy()
        maxEle = self.getMaxElement(nums)

        maxIndex = nums.index(maxEle)

        nums.pop(maxIndex)
        secMaxEle = self.getMaxElement(nums)

        if maxEle >= (secMaxEle * 2):
            return maxIndex

        return -1

    def getMaxElement(self, nums: List[int]) -> int:
        i = 0

        maxElement = nums[i]
        maxIndex = -1

        while i < len(nums):
            if maxElement < nums[i]:
                maxElement = nums[i]
                maxIndex = i
            i += 1

        return maxElement
