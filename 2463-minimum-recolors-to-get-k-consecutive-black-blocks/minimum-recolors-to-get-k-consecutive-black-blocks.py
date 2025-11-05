class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        L= 0
        window = []
        count = set()
        white_count = 0
        for ch in blocks:
            if ch =='W':
                white_count += 1

            window.append(ch)

            if len(window)>k:
                if window[0] =='W':
                    white_count -= 1
                window.pop(0)
            
            if len(window) == k:
                count.add(white_count)
        return min(count)
            
            