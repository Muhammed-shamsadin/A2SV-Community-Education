class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)

        low = 0
        high = length - 1
        ans = length

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= target:
                high = mid - 1
                ans = mid
            else:
                low = mid + 1

        return ans
                