class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def check(mid):
            days = 1
            load = 0

            for weight in weights:
                if (load + weight) > mid:
                    days += 1
                    load = weight
                else:
                    load += weight
            return days
        
        low = max(weights)
        high = sum(weights)

        while low < high:
            mid = (low + high) // 2
            if check(mid) <= days:
                high = mid
            else:
                low = mid + 1
        
        return low
