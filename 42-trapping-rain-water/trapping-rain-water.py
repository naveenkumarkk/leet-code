class Solution:
    def trap(self, height: List[int]) -> int:
        arrayLen = len(height)
        maxLeft = [0] * arrayLen
        maxRight = [0] * arrayLen

        maxLeftValue ,maxRightValue = height[0],height[arrayLen-1]
        maxWater = 0
        for i in range(1,arrayLen):
            maxLeftValue = max(maxLeftValue,height[i-1])
            maxLeft[i] = maxLeftValue
            
        
        for i in range(arrayLen-2,-1,-1):
            maxRightValue = max(maxRightValue,height[i+1])
            maxRight[i] = maxRightValue

        for i in range(arrayLen):
            water = min(maxLeft[i],maxRight[i]) - height[i]
            maxWater += max(water,0)
        return maxWater

