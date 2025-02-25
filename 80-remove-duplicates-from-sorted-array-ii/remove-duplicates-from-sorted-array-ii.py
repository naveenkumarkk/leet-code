class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashList = {}
        counter = 1
        
        for i in range(len(nums)-1,-1,-1):
            if hashList.get(nums[i]) is not None:
                if hashList[nums[i]] < counter:
                    hashList[nums[i]] = counter
            else:
                hashList[nums[i]] = counter

            if i > 0:
                if nums[i] == nums[i-1]:
                    counter +=1
                else:
                    counter = 1

        nums.clear()
        for key,value in hashList.items():
            if value >= 3:
                for i in range(2):
                    nums.append(key)
            else:
                for i in range(value):
                    nums.append(key)

        nums.reverse()


    # def removeDuplicates(self, nums: List[int]) -> int:
    #     if len(nums) <= 2:
    #         return len(nums)

    #     write_index = 2  # Start from index 2 since first two elements can stay
    #     for i in range(2, len(nums)):
    #         if nums[i] != nums[write_index - 2]:  # Allow at most two duplicates
    #             nums[write_index] = nums[i]
    #             write_index += 1

    #     # nums is now modified in place, elements beyond write_index are irrelevant
    #     return write_index
