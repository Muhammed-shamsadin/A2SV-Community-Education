class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        length = len(nums)
        pref = [0] * length
        pref[0] = nums[0]
        ans = []

        for i in range(length):
            pref[i] = pref[i-1] + nums[i]
        
        for i in range(length):
            forward = (pref[-1] - pref[i]) - (length - i - 1) * nums[i]
            backward = i * nums[i] - pref[i - 1] if i != 0 else 0

            ans.append(forward + backward)
        
        return ans