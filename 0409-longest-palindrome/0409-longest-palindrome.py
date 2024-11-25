class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        char_count = {}
        longest = 0
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
            if char_count[char] % 2 == 0:
                longest += 2
        
        if len(s) > longest:
            longest += 1
        
        return longest