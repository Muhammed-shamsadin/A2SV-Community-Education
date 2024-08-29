class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        res = 0
        curr_sum = 0
        setted = set()
        left = 0

        for right in range(length):
            while nums[right] in setted:
                setted.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

            setted.add(nums[right])
            curr_sum += nums[right]

            if curr_sum > res:
                res = curr_sum
        
        return res

