class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxlen = 0
        zeros = 0
        n = len(nums)
        l, r = 0, 0

        while r < n:
            if nums[r] == 0:
                zeros += 1
            if zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            
            length = r - l + 1
            maxlen = max(maxlen, length)
            r += 1
        
        return maxlen