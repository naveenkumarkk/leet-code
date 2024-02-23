# Thought process
# get the minimum string length of the given array elements
# check for given string index all the elements have same char
# if yes add the character to the empty string
# if the character is a mismatch store it in result string


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        arrayLength = len(strs)
        resultString = ""
        minimumStringIndex = 0
        minLength = len(strs[0])
        index = 0

        for i in range(arrayLength):
            if minLength > len(strs[i]):
                minLength = len(strs[i])
                minimumStringIndex = i

        resultString = strs[minimumStringIndex]

        strs = set(strs)
        strs.discard(minimumStringIndex)
        strs = list(strs)

        while index < len(strs) and len(resultString) != 0:
            elementString = strs[index]
            if elementString[0:minLength] != resultString:
                index = 0
                resultString = resultString[:-1]
                minLength = len(resultString)
            else:
                index += 1

        return resultString
