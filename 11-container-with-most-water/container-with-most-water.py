class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxContainer = 0
        left,right = 0,len(height) - 1

        while left < right:
            distance = right - left

            minimum = min(height[left],height[right])
            
            waterLevel = minimum * (distance )
            maxContainer = max(maxContainer,waterLevel)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxContainer



