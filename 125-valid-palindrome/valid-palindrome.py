class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = ''.join(filter(str.isalnum, s))
        cleaned_string = cleaned_string.lower()
        return cleaned_string[::-1] == cleaned_string

        # left=0
        
        # cleaned_string = ''.join(filter(str.isalnum, s))
        # cleaned_string = cleaned_string.lower()
        # right=len(cleaned_string)-1
        # while left < right  :
        #     if cleaned_string[left] != cleaned_string[right]:
        #         return False
        #     left +=1
        #     right -=1

        return True
         