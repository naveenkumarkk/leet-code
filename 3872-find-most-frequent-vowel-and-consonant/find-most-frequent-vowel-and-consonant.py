
class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_count = defaultdict(int)
        consonant_count = defaultdict(int)

        for char in s:
            if char in vowels:
                vowel_count[char] += 1
            else:
                consonant_count[char] += 1

        max_sum = 0
        if consonant_count:
            max_sum += max(consonant_count.values())
        if vowel_count:
            max_sum += max(vowel_count.values())

        return max_sum
