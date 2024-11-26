class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        length = len(nums)
        left = right = 0

        count = 0
        max_length = 0

        while left < length and right < length:
            if (left < length and right < length) and nums[right] == 0:
                count = 0
                left = right + 1
                right += 1
            if (left < length and right < length) and nums[right] == 1:
                count += 1
                right += 1

            max_length = max(count, max_length)

        return max_length