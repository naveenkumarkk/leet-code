class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def f(piles, k):
            return  sum ( [ math.ceil(p / k) for p in piles ] )

        k_min = 1
        k_max = max(piles)
        if k_min <= 0 or f(piles, k_max) > h:
            return
        
        if f(piles, k_min) < h:
            return k_min 
        
        L = k_min
        R = k_max
        res = k_max

        while L <= R :

            mid = ( L + R ) // 2

            if f(piles, mid) > h :
                L = mid + 1
            else :
                res = min(res, mid)
                R = mid - 1
        
        return res