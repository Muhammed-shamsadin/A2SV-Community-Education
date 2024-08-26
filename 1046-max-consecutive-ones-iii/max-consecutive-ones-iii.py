class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        length = len(nums)

        zeros = 0
        max_len = 0
        right = 0
        left = 0

        while right < length:
            if nums[right] == 0:
                zeros += 1
            
            if zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            if zeros <= k:
                current_length = right - left + 1
                max_len = max(max_len, current_length)

            right += 1
        return max_len
        