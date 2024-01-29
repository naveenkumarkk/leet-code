class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = 0
        result = []
        for num in nums:
            running_sum += num
            result.append(running_sum)

        return result