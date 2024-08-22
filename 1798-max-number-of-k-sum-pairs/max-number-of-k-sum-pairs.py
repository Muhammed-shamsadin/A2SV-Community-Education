class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        length = len(nums)

        max_operation = 0
        left = 0 
        right = length - 1  

        while left < right:
            if nums[left] + nums[right] == k:
                max_operation += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                left += 1

        return max_operation

            