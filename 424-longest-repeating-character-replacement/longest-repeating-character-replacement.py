from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dictionary = defaultdict(int)
        left = 0
        res = 0
        for right in range(len(s)):
            dictionary[s[right]] += 1
            maxLen = max(dictionary.values())
            currentLen = right - left + 1

            if currentLen -  maxLen > k:
                dictionary[s[left]] -= 1
                left += 1
            
            res = max(res,right-left +1)
        return res
            
