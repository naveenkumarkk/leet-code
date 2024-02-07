class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n=len(nums)
        lastEvenOrder = 0
        lastOddOrder = 0
        result = []
        for i in range(n):
            if nums[i] % 2 == 0:
                result.insert(lastEvenOrder,nums[i])
                lastEvenOrder+=1
            else:
                result.append(nums[i])

        return result