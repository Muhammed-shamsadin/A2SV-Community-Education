class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = 0
        
        for i in range(n):
            if nums[left] != 0:
                left += 1
            else:
                if nums[i] != 0:
                    nums[i], nums[left] = nums[left], nums[i]
                    left += 1
            