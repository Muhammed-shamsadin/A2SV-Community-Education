class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        op = []
        nums.sort()
        for i in range(n):
            if nums[i] == target:
                op.append(i)
        
        return op