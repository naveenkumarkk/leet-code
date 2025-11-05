class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r = 0,k-1
        minimum_diff = float('inf')
        while r < len(nums):
            minimum_diff = min(minimum_diff,nums[r]-nums[l])
            l+=1
            r+=1
        return minimum_diff