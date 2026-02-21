class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left = 0
        right = 0
        nums1Length = len(nums1)
        nums2Length = len(nums2)
        sortedArray = []

        while left < nums1Length and right < nums2Length:
            if nums1[left] <= nums2[right]:
                sortedArray.append(nums1[left])
                left += 1
            elif nums1[left] > nums2[right]:
                sortedArray.append(nums2[right])
                right += 1

        if nums1[left:] :
            sortedArray.extend(nums1[left:])
        if nums2[right:]:
            sortedArray.extend(nums2[right:])

        sortedArrayLength = len(sortedArray) 
        mid = sortedArrayLength // 2
        if sortedArrayLength % 2 == 0:
            return (sortedArray[mid - 1] + sortedArray[mid]) / 2
        else:
            return sortedArray[mid]
