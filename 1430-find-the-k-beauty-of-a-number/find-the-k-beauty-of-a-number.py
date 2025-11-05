class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count = 0
        string_num = str(num)
        for R in range(len(string_num)-k+1):
            sub_num = int (string_num[R:R+k])
            if sub_num > 0 and num % sub_num == 0:
               count+=1  

        return count