class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)

        for char in s:
            count[char] += 1
        for i,c in enumerate(s):
            if count[c] == 1:
                return i
        return -1