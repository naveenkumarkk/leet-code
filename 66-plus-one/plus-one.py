class Solution:
    # Thought Process:
    # multiply with its units place
    # and sum it up
    # add 1
    # divide the elemts to get it its

    def plusOne(self, digits: List[int]) -> List[int]:
        
        i = len(digits) - 1
        multiplier = 1
        total = 0
        resultArray = []

        while i >= 0:
            digitNumber = digits[i] * multiplier
            total += digitNumber
            multiplier *= 10
            i -= 1

        total += 1

        for ch in str(total):
            resultArray.append(int(ch))

        return resultArray
