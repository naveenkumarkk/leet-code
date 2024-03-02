class Solution:
    def reverseWords(self, s: str) -> str:
        
        tempCharacter = ''
        reversedString = ''
        
        for i in range(0,len(s),1):
            if i is len(s) or s[i] is ' ':
                reversedString += tempCharacter[::-1] + ' '
                tempCharacter = ''
            else: tempCharacter += s[i]

        reversedString += tempCharacter[::-1]

        return reversedString

        