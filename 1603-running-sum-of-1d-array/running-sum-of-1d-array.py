class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pre = [] 
        summ = 0

        for i in range(len(nums)):
            summ += nums[i]
            pre.append(summ)
        
        return pre
        