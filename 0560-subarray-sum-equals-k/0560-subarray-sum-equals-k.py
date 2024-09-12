class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        length = len(nums)
        
        count = 0
        pref = 0
        pref_count = {0 : 1}

        for i in nums:
            pref += i

            if (pref - k) in pref_count:
                count += pref_count[pref - k]
            if pref in pref_count:
                pref_count[pref] += 1
            else:
                pref_count[pref] = 1
        
        return count
        
        