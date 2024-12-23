class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        length = len(nums)
        maxmimumSum = 0
        nums.sort()


        for i in range(length // 2):
            minimum = min(nums[i + i], nums[i + i])
            maxmimumSum += minimum

        return maxmimumSum