class Solution:
   def validMountainArray(self, a: List[int]) -> bool:
        start, end, L = 0, -1, len(a)

        while start < L-1 and a[start] < a[start+1]: 
            start += 1
        while end > -L and a[end] < a[end-1]: 
            end -= 1

        return start == end + L and 0 < start and end < -1