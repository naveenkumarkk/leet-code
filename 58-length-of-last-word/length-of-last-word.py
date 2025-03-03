class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        count = 0
        start = 0
        end = 0
        sarray = []
        for i in range(len(s)):
            if (s[i] == ' ' or i == len(s)-1) :
                end = i+1
                sarray.append(s[start:end])
                start=i+1
        print(sarray)
        
        for j in range(len(sarray)-1,-1,-1):
            if sarray[j] != ' ' and sarray[j] !='' :
                return len(sarray[j].strip())
        # x = s.split()
        # last_word = x[-1]

        # return len(last_word)