class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        k = int(sqrt(c))
        left, right = 0, k
        while left <= right:
            res = (left * left) + (right * right)
            if res > c:
                right -= 1
            elif res < c:
                left += 1
            else:
                return True
        
        return False