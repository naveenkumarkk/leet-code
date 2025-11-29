class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        if nums[right] != len(nums):
            return len(nums)
        
        while left <= right:
            if nums[right]-1 != nums[right-1]:
                return nums[right]-1
            right -= 1

        