class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        character_index =  []
        for i,word in enumerate(words):
            if x in word:
                character_index.append(i)
        return character_index
        