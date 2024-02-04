class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = m-1
        b = n-1
        newIndex = m+n-1
        while b>=0:
            if a>=0 and nums1[a] > nums2[b]:
                nums1[newIndex] = nums1[a]
                a -=1
            else:
                nums1[newIndex] = nums2[b]
                b -= 1
            newIndex -=1

