class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n_len = len(needle)
        for i in range(len(haystack) - n_len + 1):
                if haystack[i:i+n_len] == needle: return i
        return -1

        
       