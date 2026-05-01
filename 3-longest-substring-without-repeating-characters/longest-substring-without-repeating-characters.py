class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        last_seen = set()
        maxLength = float("-inf")
        left = 0

        for right,char in enumerate(s):
            while char in last_seen:
                last_seen.remove(s[left])
                left += 1

            last_seen.add(char)
            maxLength = max(maxLength,right - left + 1)

        return maxLength