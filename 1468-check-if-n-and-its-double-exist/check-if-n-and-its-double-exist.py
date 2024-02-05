class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        i = 0
        n = len(arr)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if self.checkCondtions(arr[i], arr[j]):
                    return True

        return False

        return resultState

    def checkCondtions(self, i: int, j: int) -> bool:
        return (i != j and (i == 2 * j or j == 2*i)) or (i is 0 and j is 0)
