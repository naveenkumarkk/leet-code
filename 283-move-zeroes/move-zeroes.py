class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        last_non_zero_index = 0

        # Move all non-zero elements to the front
        for i in range(n):
            if nums[i] != 0:
                nums[last_non_zero_index] = nums[i]
                last_non_zero_index += 1

            # Fill the remaining positions with zeros
        while last_non_zero_index < n:
                nums[last_non_zero_index] = 0
                last_non_zero_index += 1
