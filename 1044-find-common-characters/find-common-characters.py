class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_char = []

        first_Word = set(words[0])

        for char in first_Word:
            freq = min([word.count(char) for word in words])
            common_char += [char] * freq
        
        return common_char