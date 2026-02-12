class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(nlongn)
        ans = []
        for key,value in enumerate(nums):
            if key > 0 and value == nums[key-1]:
                continue
            left, right = key + 1 ,len(nums) -1 

            while left < right:
                threeSum = value + nums[left] + nums[right]
                if threeSum == 0:
                    ans.append([value,nums[left],nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif threeSum > 0:
                    right -= 1
                else:
                    left += 1
        return ans