class Solution:
    def isGood(self,s:str) ->bool:
        return (s[0] != s[1] and  s[0] != s[2] and s[1] != s[2])

    def countGoodSubstrings(self, s: str) -> int:
        L = 0
        count = 0
        for i in range(len(s)):
            if len(s[i:]) > 2:
                sub_string = s[i:i+3]
                if self.isGood(sub_string): count+= 1
        return count
