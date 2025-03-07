class Solution:
    def intToRoman(self, num: int) -> str:
        system = [
            ["I", 1],
            ["IV", 4],
            ["V", 5],
            ["IX", 9],
            ["X", 10],
            ["XL", 40],
            ["L", 50],
            ["XC", 90],
            ["C", 100],
            ["CD", 400],
            ["D", 500],
            ["CM", 900],
            ["M", 1000],
        ]
        result = ""
        for sys,val in reversed(system):
            if num//val:
                count = num // val
                result += (sys * count)
                num = num % val
        return result