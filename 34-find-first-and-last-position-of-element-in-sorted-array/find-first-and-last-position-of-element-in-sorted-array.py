class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def BinarySearch(nums, target, searching_left):
            low = 0
            high = len(nums) - 1
            ans = -1

            while low <= high:
                mid = (low + high) // 2
                

                if nums[mid] > target:
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    ans = mid
                    if searching_left:
                        high = mid - 1
                    else:
                        low = mid + 1

            return ans
        
        first = BinarySearch(nums, target, True)
        last = BinarySearch(nums, target, False)

        return [first, last]
            

            