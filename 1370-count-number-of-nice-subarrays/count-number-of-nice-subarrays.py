class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        length = len(nums)
        left = 0
        count = 0
        res = 0

        for right in range(length):
            if nums[right] % 2:
                k -= 1
                count = 0
            while not k:
                k += (nums[left] % 2)
                count += 1
                left += 1
            res += count
        return res
