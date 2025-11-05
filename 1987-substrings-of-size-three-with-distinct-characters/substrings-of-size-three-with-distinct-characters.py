class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        window = []

        for ch in s:
            window.append(ch)
            if len(window) > 3:
                window.pop(0)
            if len(window) == 3 and len(set(window)) == 3:
                count += 1
        return count
