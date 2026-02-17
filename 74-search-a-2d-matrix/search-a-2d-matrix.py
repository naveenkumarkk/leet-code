class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rowLen = len(matrix)
        columnLen = len(matrix[0])

        low,high = 0, (rowLen * columnLen) - 1

        while low <= high:
            mid = (low + high) // 2
            row = mid // columnLen
            col = mid % columnLen

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False