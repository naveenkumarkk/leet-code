from collections import deque

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        count = 0
        window = deque()

        for ch in s:
            window.append(ch)

            if len(window) > k:
                window.popleft()

            if len(window) == k:
                sub_num = int("".join(window))
                if sub_num>0 and num % sub_num ==0:
                    count+=1
        return count