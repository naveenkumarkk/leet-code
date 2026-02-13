class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_water = 0
        while left < right:
            area = max(right,left) - min(right,left)
            if height[left] < height[right]:
                min_value = height[left]
                left += 1
            else:
                min_value = height[right]
                right -= 1
            trapped_water = min_value * area
            
            max_water = max(max_water,trapped_water)
        return max_water
