class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        aLength = len(a)
        bLength = len(b)
        carry = 0
        res = ""
        for i in range(max(aLength, bLength)):
            sumValue = carry
            digitA = ord(a[i]) - ord("0") if i < aLength else 0
            digitB = ord(b[i]) - ord("0") if i < bLength else 0
            sumValue = digitA + digitB + carry

            char = str(sumValue % 2)
            res = char + res
            carry = sumValue // 2
        if carry:
            res = "1" + res
        return res
