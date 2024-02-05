class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        i = 0

        resultState = False
        while i < len(arr) - 1:
            j = i + 1
            while j <= len(arr) - 1:
                conditioncheck = self.checkCondtions(arr[i], arr[j])
                if conditioncheck:
                    resultState = True
                    break
                j += 1
                if resultState is True:
                    break
            if resultState is True:
                break
            i += 1

        return resultState

    def checkCondtions(self, i: int, j: int) -> bool:
        return (i != j and (i == 2 * j or j == 2*i)) or (i is 0 and j is 0)
