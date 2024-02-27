# Thought Process
# Sort the array
# using sliding window approach find the target value and return the count


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length, left, right = 999999, 0, 0
        arrayLength = len(nums)
        summation = 0

        while right < arrayLength:
            summation += nums[right]
            if summation >= target:
                while summation >= target:
                    summation -= nums[left]
                    left += 1
                length = min(length, right - left + 2)
            right += 1

        if length == 999999:
            return 0
        return length
