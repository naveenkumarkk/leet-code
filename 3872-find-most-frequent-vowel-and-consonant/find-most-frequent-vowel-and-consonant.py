class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels_dict = {
            'a':0,
            'e':0,
            'i':0,
            'o':0,
            'u':0
        }
        constant_dict = {}

        for char in s:
            if char in vowels_dict:
                vowels_dict[char] += 1
            else:
                if char in constant_dict:
                    constant_dict[char] += 1
                else:
                    constant_dict[char] = 1
        max_value = 0
        if any(constant_dict):
            max_value += max(constant_dict.values())

        if any(vowels_dict):
            max_value += max(vowels_dict.values())
        
        return max_value


