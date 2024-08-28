class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums)

        left = 0
        total = 0
        res = float("inf")

        for right in range(length):
            total += nums[right]

            while total >= target:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1
            
        if res == float("inf"):
            return 0
        else:
            return res
