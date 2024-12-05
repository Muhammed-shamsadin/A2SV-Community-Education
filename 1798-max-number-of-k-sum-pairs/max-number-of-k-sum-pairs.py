class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        length = len(nums)
        left, right = 0, length - 1
        cnt = 0
        nums.sort()

        while left < right:
            if nums[right] + nums[left] == k:
                cnt += 1
                left += 1
                right -= 1
            elif nums[right] + nums[left] > k:
                right -= 1
            else:
                left += 1

        return cnt
