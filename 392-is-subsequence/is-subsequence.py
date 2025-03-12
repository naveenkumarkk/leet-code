class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        slen = len(s)
        tlen = len(t)

        spointer,tpointer = 0,0

        while spointer < slen and tpointer< tlen:
            if s[spointer] == t[tpointer]:
                spointer += 1
            tpointer +=1
       
        if spointer == slen:
            return True

        return False