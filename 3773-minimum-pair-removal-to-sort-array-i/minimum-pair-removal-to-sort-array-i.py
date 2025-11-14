class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operation_count = 0

        while len(nums) > 1:
            is_sorted = True

            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    is_sorted = False
                    break

            if is_sorted:
                break
            
            operation_count += 1

            minimum_sum = float('inf')
            minimum_index = -1

            for i in range(len(nums)-1):
                if minimum_sum > (nums[i] + nums[i+1]):
                    minimum_sum = nums[i] + nums[i+1]
                    minimum_index = i
            nums[minimum_index:minimum_index+2] = [minimum_sum]


        return operation_count
