class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        result = 0
        pref_sum = 0
        my_dict = defaultdict(int)
        my_dict[0] = 1

        for num in nums:
            pref_sum += num
            remainder = pref_sum % k

            if remainder in my_dict:
                result += my_dict[remainder]
            
            my_dict[remainder] += 1
        
        return result