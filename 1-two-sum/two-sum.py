class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}
        

        for i,n in enumerate(nums):
            remainder = target - n

            if remainder in hashMap:
                return [i,hashMap[remainder]]
            hashMap[n] = i
            