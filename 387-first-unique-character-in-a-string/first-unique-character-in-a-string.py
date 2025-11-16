class Solution:
    def firstUniqChar(self, s: str) -> int:
        index_count = 0
        poped_string = ''
        while len(s) > 0:
            check_character = s[0]
            if s[0] not in s[1:] and s[0] not in poped_string:
                return index_count
            poped_string = poped_string+s[0]
            s = s[1:]
            index_count += 1
        
        return -1