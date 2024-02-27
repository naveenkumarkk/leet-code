# Thought Process
# Sort the array
# using sliding window approach find the target value and return the count


class Solution:
      def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        arrayLength = len(nums)
        minLength = float('inf')  # Initialize minLength to positive infinity
        left = 0
        summation = 0

        for right in range(arrayLength):
            summation += nums[right]
            while summation >= target:
                minLength = min(minLength, right - left + 1)
                summation -= nums[left]
                left += 1

        # If minLength is still infinity, it means no subarray was found
        return minLength if minLength != float('inf') else 0