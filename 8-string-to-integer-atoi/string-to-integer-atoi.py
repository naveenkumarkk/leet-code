class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0

        result = 0
        is_negative = 1
        i = 0

        # Check for sign
        if s[0] == '-':
            is_negative = -1
            i += 1
        elif s[0] == '+':
            i += 1

        # Parse digits
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result = is_negative * result

        # Clamp to 32-bit signed int range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        elif result > INT_MAX:
            return INT_MAX
        else:
            return result
