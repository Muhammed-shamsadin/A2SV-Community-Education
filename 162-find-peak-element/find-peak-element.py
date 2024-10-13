class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        length = len(nums)
        low,high = 0, length - 1

        while low <= high:
            mid = (low + high) // 2

            if mid > 0 and nums[mid] < nums[mid - 1]:
                high = mid - 1
            elif mid < length - 1 and nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                return mid