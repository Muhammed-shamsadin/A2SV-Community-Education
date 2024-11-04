class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def tot(mid):
            total = 0
            for i in range(len(piles)):
                total += math.ceil (piles[i] / mid)
            return total <= h
        
        low, high = 1, max(piles)
        while low <= high:
            mid = (low + high) // 2
            if tot(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low