class Solution:
    def replaceElements(self,arr: List[int]) -> List[int]:
        n = len(arr)
        max_element = -1

        for i in range(n - 1, -1, -1):
            current_element = arr[i]
            arr[i] = max_element
            max_element = max(max_element, current_element)

        return arr
