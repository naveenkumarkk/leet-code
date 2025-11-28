class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        
        def is_strictly_increasing(nums: list[int])->bool:
            for i in range(1,len(nums)):
                if nums[i] <= nums[i-1]:
                    return False
            return True
        array_len = len(nums)
        left,right = 0, 0
        count = 0
        while left < array_len:
            while right < array_len:
                if is_strictly_increasing(nums[:left]+nums[right+1:array_len]) == True:
                    count += 1
                right += 1
            left += 1
            right = left
        return count