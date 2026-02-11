class Solution:
    def checkNumberIsStartSequence(self,number:int,nums:set) ->bool:
        return number - 1 not in nums

    def checkNumberHasNext(self,number:int,nums:set) ->bool:
        return number + 1 in nums

    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        set_array = set(nums)
        count = 0
        max_count = 0

        for n in set_array:
            if self.checkNumberIsStartSequence(n,set_array):
                length = 1
                current = n
                while self.checkNumberHasNext(current,set_array):
                    current += 1
                    length += 1
                
                max_count = max(max_count,length)
        return max_count