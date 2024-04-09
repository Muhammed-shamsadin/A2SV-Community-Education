class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        a = x[::-1]
        return a == x