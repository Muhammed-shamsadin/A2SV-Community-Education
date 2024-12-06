class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        prefix_len = len(searchWord)
        for i in range(len(words)):
            # print(words[i][:prefix_len])
            if searchWord in words[i] and words[i][:prefix_len] == searchWord:
                return i + 1
        return -1
            