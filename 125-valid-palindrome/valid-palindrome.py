class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for char in s:
            if char.isalpha() or char.isdigit():
                res.append(char.lower())
        print(res)
        right = len(res) - 1
        left = 0

        while left <= right:
            if res[left] != res[right]:
                return False
            right -= 1
            left += 1

        return True 