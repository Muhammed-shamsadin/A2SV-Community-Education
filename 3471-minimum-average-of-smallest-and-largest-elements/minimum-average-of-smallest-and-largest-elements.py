class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = len(nums)

        l = 0
        r = n - 1
        averages = []

        while l < r:
            k = (nums[l] + nums[r]) / 2
            averages.append(k)

            l += 1
            r -= 1

        return(min(averages))
