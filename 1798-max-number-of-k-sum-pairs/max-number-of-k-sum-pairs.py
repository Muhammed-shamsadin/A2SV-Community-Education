class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        count = 0
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] + nums[right] == k:
                count += 1
                right -= 1
                left += 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                 left += 1
           
        
        return count
            