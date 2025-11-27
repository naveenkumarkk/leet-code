class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        left = 0
        right = left + 1
        count = 0
        while left < len(nums)-1:
            if nums[left] + nums[right] < target:
                count += 1
            right += 1

            if right == len(nums):
                left +=1 
                right = left + 1
        return count 
                