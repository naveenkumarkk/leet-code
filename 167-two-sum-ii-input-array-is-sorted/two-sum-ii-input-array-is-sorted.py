# Thought Process:
# Given array is sorted
# I need to add two elements which equal to the given target in an array and return those indexes
# I can omit the array elements which are grater then the target
# Edge Case:But if there are only two elements in an array I should consider 0 as well
# I need to iterate through each index element and add it to the next all elements and see if the sum is
# is equal to the target


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []

        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]  # Adjusting indexes to 1-based indexing
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return []

    def checkSum(self, num1: int, num2: int, target: int):
        return target == (num1 + num2)
