class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        n = len(s)
        l = 0
        r = n - 1

        new_s = list(s)
        
        
        while l < r:
            if new_s[l] in vowels and new_s[r] in vowels:
                new_s[l], new_s[r] = new_s[r], new_s[l]
                l += 1
                r -= 1
            if new_s[l] not in vowels:
                l += 1
            
            if new_s[r] not in vowels:
                r -= 1

        return ''.join(new_s) 
