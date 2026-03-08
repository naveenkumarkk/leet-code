class Solution:

    def checkIfNumHasNext(self,n,nums:set)->bool:
        return n + 1 in nums

    def checkIfNumisStartSequence(self,n,nums:set)->bool:
        return n - 1 not in nums

    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength = 0
        if len(nums) == 0:
            return 0
        nums = set(nums)
        for n in nums:
            if self.checkIfNumisStartSequence(n,nums):
                length = 1
                current = n
                while self.checkIfNumHasNext(current,nums):
                    length += 1
                    current += 1
                maxLength = max(maxLength,length)

        return maxLength

        # If Input is positive the following code works
        # hashMap = {}
        # if len(nums) == 0:
        #     return 0
        # maxEle = max(nums)
        # bucket = [0] * (maxEle + 1)

        # for i in range(len(nums)):
        #     if nums[i] in hashMap:
        #         hashMap[nums[i]]+= 1
        #     else:
        #         hashMap[nums[i]] = 1
        
        # for key,value in hashMap.items():
        #     bucket[key] = value

        # maxCount = 0
        # count = 0
        
        # for index,value in enumerate(bucket):

        #     if value == 0:
        #         maxCount = max(maxCount,count)
        #         count = 0
        #     else:
        #         count += 1
        # maxCount = max(maxCount,count)
        # return maxCount