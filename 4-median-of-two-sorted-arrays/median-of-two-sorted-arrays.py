class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # left = 0
        # right = 0
        # nums1Length = len(nums1)
        # nums2Length = len(nums2)
        # sortedArray = []

        # while left < nums1Length and right < nums2Length:
        #     if nums1[left] <= nums2[right]:
        #         sortedArray.append(nums1[left])
        #         left += 1
        #     elif nums1[left] > nums2[right]:
        #         sortedArray.append(nums2[right])
        #         right += 1

        # if nums1[left:] :
        #     sortedArray.extend(nums1[left:])
        # if nums2[right:]:
        #     sortedArray.extend(nums2[right:])

        # sortedArrayLength = len(sortedArray) 
        # mid = sortedArrayLength // 2
        # if sortedArrayLength % 2 == 0:
        #     return (sortedArray[mid - 1] + sortedArray[mid]) / 2
        # else:
        #     return sortedArray[mid]

        A,B = nums1, nums2

        if len(B) < len(A):
            A,B = B,A
        total=len(A) + len(B)
        half=total//2

        l,r=0,len(A)-1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i>= 0 else float("-inf")
            Aright = A[i+1] if (i+1) < len(A) else float("inf")
            Bleft = B[j] if j>= 0 else float("-inf")
            Bright = B[j+1] if (j+1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft<=Aright:
                if total % 2:
                    return min(Aright,Bright)
                return (max(Aleft,Bleft)+min(Aright,Bright))/2
            elif Aleft>Bright:
                r=i-1
            else:
                l=i+1