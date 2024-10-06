class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Approach: Binary Search (logN)
        ''' 
        length = len(nums)

        # step 1: intialize the low and high pointers
        low = 0
        high = length - 1
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                ans = mid
                return ans
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return -1