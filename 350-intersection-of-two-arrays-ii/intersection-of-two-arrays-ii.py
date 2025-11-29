class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        minList = nums1 if len(nums1) <= len(nums2) else nums2
        maxList = nums1 if len(nums1) > len(nums2) else nums2
        ans = []
        
        for num in maxList:
            if num in minList:
                ans.append(num)
                minList.remove(num)
        return ans