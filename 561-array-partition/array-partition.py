class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        length = len(nums)
        minimum = 0
        nums.sort()

        for i in range(length // 2):
            minimum += nums[i*2]

        return minimum