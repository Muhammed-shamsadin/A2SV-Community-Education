class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # TC: O(N)
        # SC: O(1)

        xor = 0

        for num in nums:
            xor ^= num
        return xor
        