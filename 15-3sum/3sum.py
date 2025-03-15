class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()       
        res = []

        for i,a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            j,k = i+1,len(nums)-1

            while j < k:
                threesum = nums[i] + nums[j] + nums[k]

                if threesum > 0:
                    k -=1
                elif threesum < 0:
                    j +=1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while nums[j] == nums[j-1] and j < k:
                        j+=1
        return res

            




