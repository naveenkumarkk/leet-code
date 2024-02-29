# Thought Process:
# Initialise left Pointer at the begining of the array
# Initialise roght pointer at the end of the array
# swap the pointer values until it both equal
class Solution:
    def reverseWords(self, s: str) -> str:
        stringArray = s.strip().split()
        left , right = 0,len(stringArray)-1

        while left<=right:
            temp = stringArray[left]
            stringArray[left] = stringArray[right]
            stringArray[right] = temp
            left+=1
            right-=1
        
        return ' '.join(stringArray)

