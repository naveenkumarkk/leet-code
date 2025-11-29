class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2: return True
        left = 1
        right = num // 2
        
        while left <= right:
            mid = (left + right)//2
            att_sqr = mid * mid
            if att_sqr == num:
                return True
            elif att_sqr < num :
                left = mid + 1
            else:
                right = mid - 1
        return False

