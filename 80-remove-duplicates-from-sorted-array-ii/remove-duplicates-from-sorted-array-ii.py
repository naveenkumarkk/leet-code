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
