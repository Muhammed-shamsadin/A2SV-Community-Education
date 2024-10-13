class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        length = len(nums)

        # Edge cases:
        if length == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[length - 1] != nums[length - 2]:
            return nums[length - 1]

        low, high = 1, length - 2

        while low <= high:
            mid = (low + high) // 2

            if (nums[mid] != nums[mid + 1]) and (nums[mid - 1] != nums[mid]):
                return nums[mid]
            if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
                low = mid + 1
            else:
                high = mid - 1
        
        return -1

            