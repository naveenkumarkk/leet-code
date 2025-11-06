class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        max_count = 0
        i = 0

        while i < len(nums):
            j = i+1

            if nums[i] <= threshold and nums[i]%2 == 0 :
                while j < len(nums) and nums[j]<= threshold and nums[j] % 2 != nums[j-1] %2:
                    j += 1
                max_count = max(max_count,j-i)
            i = j
        return max_count