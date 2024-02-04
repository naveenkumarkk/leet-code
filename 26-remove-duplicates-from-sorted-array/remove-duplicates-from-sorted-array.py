class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        result = []
        i= 0
        j = 1
        result.append(nums[0])
        while i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                result.append(nums[i+1])
            i+=1
            
        nums[:len(result)] = result

        return len(result)