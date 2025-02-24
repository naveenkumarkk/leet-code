class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m < len(nums1):
            del nums1[m:]
        
        if n < len(nums2):
            del nums2[n:]

        for index,value in enumerate(nums2):
            nums1.append(value)
        
        nums1.sort()
                

       
        
       
             



        