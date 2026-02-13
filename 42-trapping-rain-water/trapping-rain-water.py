class Solution:
    def trap(self, height: List[int]) -> int:
        # trapped_water = 0

        # for i in range(1,len(height)):
        #     leftMax = max(height[:i])
        #     rightMax = max(height[i:]) 
        #     trapped_water += max(min(leftMax,rightMax) - height[i],0)

        # return trapped_water
        left,right = 0,len(height)-1
        leftMax,rightMax = height[left],height[right]
        res = 0

        while left < right:
            if leftMax < rightMax:
                left += 1
                res += max(leftMax - height[left],0)
                leftMax = max(leftMax,height[left])
            else:
                right -= 1
                res += max(rightMax - height[right],0)
                rightMax = max(rightMax,height[right])
        return res
        

                