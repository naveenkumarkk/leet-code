class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        array_len = len(numbers) - 1
        right = len(numbers) - 1
        left = 0

        while left < right:
            temp_sum = numbers[left] + numbers[right]
            if temp_sum == target:
                return [left+1,right+1]
            elif temp_sum > target:
                right -= 1
            else:
                left += 1
        
