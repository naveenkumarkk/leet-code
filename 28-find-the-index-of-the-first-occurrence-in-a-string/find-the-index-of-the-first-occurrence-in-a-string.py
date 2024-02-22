# Thought Process
# we need to search given input word is present in the given line
# If nothing is present return -1
# if yes return the start of the index
# so the given entire word should be present in a continuous

# construct a string till the length of the input string


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
            if not needle: return 0
            n_len = len(needle)
            for i in range(len(haystack) - n_len + 1):
                if haystack[i:i+n_len] == needle: return i
            return -1

