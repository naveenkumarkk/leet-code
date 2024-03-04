

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowArray = []
        for row in range(0, rowIndex + 1):
            ans = self.findNcr(rowIndex, row)
            rowArray.append(ans)
        return rowArray

    def findNcr(self, n: int, r: int) -> int:
        if r > n - r:
            r = n - r
        ans = 1
        for i in range(r):
            ans *= (n - i)
            ans //= (i + 1)
        return ans