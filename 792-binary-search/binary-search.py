class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        mid = len(nums) // 2
        print(mid)
        if nums[mid] <= target:
            while mid < len(nums):
                if nums[mid] == target:
                    return mid
                mid += 1
        elif nums[mid] > target:
            start = 0
            while start < mid:
                if nums[start] == target:
                    return start
                start += 1
        return -1