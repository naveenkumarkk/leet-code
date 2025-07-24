class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for chars in stones:
            if chars in jewels:
                count += 1
        return count
        

