class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1 
        minimum = float("inf")
        if len(nums) < 2:
            return nums[0]
        while low < high:
            mid = (low + high) // 2
            # print("low=>",low,"=>",nums[low],"mid=>",mid,"=>",nums[mid],"high=>",high,"=>",nums[high])
            
            if nums[mid] < nums[high]:
                high = mid
            else:
                low = mid + 1
                
            if nums[low] == nums[high]:
                return nums[low]
