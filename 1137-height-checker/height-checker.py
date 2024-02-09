class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        arrayLength = len(heights)
        matchDifferenceCount = 0
        oldArray = []
        oldArray = heights.copy()
        for i in range(0, arrayLength):
            for j in range(i, arrayLength):
                if heights[i] > heights[j]:
                    tempElement = heights[i]
                    heights[i] = heights[j]
                    heights[j] = tempElement

            if oldArray[i] != heights[i]:
                matchDifferenceCount += 1
        return matchDifferenceCount
