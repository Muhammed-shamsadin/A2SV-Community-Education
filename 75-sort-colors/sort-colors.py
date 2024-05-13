class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt_of_zeros = nums.count(0)
        cnt_of_ones = nums.count(1)

        for i in range(len(nums)):
            if cnt_of_zeros > 0:
                nums[i] = 0
                cnt_of_zeros -= 1
            elif cnt_of_ones > 0:
                nums[i] = 1
                cnt_of_ones -= 1
            else:
                nums[i] = 2
            



