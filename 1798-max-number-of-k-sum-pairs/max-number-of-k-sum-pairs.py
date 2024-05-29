class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        from collections import defaultdict

        # int gives 0 when not found
        complements = defaultdict(int)
        ops = 0
        for n in nums:
            if complements[n] > 0:
                ops += 1
                complements[n] -= 1
            elif n < k:
                complement = k - n
                complements[complement] += 1
        return ops
        