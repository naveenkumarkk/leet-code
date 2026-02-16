class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for key,value in enumerate(heights):
            start = key
            while stack and stack[-1][0] > value:
                height,index = stack.pop()
                w = key - index
                area = height * w
                maxArea = max(maxArea,area)
                start = index
            stack.append((value,start))

        for h,i in stack:
            maxArea = max(maxArea,h * (len(heights) - i))
        return maxArea
