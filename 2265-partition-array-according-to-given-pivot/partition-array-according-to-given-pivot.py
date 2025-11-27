class Solution:       
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        left_array = []
        pivot_array = []
        greatr_array = []
        for i in range(len(nums)):
            if nums[i] < pivot:
                left_array.append(nums[i])
            elif nums[i] == pivot:
                pivot_array.append(nums[i])
            else:
                greatr_array.append(nums[i])
        return left_array + pivot_array + greatr_array

        