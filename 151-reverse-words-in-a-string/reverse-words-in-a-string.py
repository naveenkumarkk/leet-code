class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        text = s.split()
        text.reverse()
        return " ".join(text)

