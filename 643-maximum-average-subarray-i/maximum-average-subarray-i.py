class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        total = sum(nums[:k])
        maximum = total 

        for i in range(k, n):
            total += nums[i] - nums[i - k]
            maximum = max(maximum, total)

        return maximum / k

        





















        
