class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        length = len(s)
        vowels = ['a', 'e', 'i', 'o', 'u']

        max_vowel = 0
        curr_vowels = 0
        left = 0
        right = 0

        while right < length:
            if s[right] in vowels:
                curr_vowels += 1
            if right - left + 1 > k:
                if s[left] in vowels:
                    curr_vowels -= 1
                left += 1

            max_vowel = max(max_vowel, curr_vowels)

            right += 1
        return max_vowel
