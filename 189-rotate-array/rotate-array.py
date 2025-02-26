class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for num in range(k):
            removedElement = nums.pop()
            nums.insert(0,removedElement)


# def rotate(nums: List[int], k: int) -> None:
#     """
#     Rotates the array to the right by k steps.
#     This solution runs in O(n) time and O(1) space.
#     """
#     k %= len(nums)  # Handle cases where k is larger than length of nums
#     nums[:] = nums[-k:] + nums[:-k]  # Slice and concatenate
