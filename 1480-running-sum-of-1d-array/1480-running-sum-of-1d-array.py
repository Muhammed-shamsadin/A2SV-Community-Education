class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        length = len(nums)
        pref = [0] * length

        pref[0] = nums[0]

        for i in range(1, length):
            pref[i] = pref[i - 1] + nums[i]
        
        return pref