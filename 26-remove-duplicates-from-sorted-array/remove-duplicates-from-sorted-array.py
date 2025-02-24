class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        counter = len(nums)

        for index in range(len(nums)-2,-1,-1):
            if nums[index] == nums[index + 1]:
                nums.pop(index)
                counter -= 1            
        return counter
        