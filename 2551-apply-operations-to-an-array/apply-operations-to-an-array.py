class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        zeros = 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
        
        zeros = nums.count(0)
        nums = [i for i in nums if i != 0]
        return nums + ([0] * zeros)
