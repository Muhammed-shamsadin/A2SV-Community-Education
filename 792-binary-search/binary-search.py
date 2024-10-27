class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        low = 0
        high = length - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
                break
            else:
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return -1