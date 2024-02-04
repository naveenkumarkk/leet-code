from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        arrayLength = len(nums)
        result = []

        for i in range(arrayLength):
            if nums[i] != val:
                result.append(nums[i])

        nums[:len(result)] = result

        return len(result)
