class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        for index in range(len(nums)-1,-1,-1):
            if val == nums[index]:
                nums.remove(val)
        
        return len(nums)