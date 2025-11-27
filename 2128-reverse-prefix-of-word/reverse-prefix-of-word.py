class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        if ch not in word: 
            return word
        else:
            index = word.find(ch)
            sub_string = word[0:index+1]
            
            return sub_string[::-1] + word[index+1:]

