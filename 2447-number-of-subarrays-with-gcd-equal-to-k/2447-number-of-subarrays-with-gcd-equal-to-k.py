class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        length = len(nums)
        ans = 0
        for i in range(length):
            temp = nums[i]
            for j in range(i, length):
                temp = math.gcd(temp, nums[j])
                if temp == k:
                    ans += 1
                elif temp < k:
                    break
        return ans