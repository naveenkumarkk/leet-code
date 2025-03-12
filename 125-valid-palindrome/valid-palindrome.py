class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        convertedString = ''
        for char in s:
            if char.isalnum():
              convertedString+=char 
        
        first, last = 0,len(convertedString)-1

        while first < last:
            if first >= last or convertedString[first] != convertedString[last] :
                return False
            first +=1
            last -= 1
        return True
