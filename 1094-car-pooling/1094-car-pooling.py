class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        length = len(trips)
        pref = [0] * (max(trips, key = lambda x:x[2])[2] + 1)

        for i in range(length):
            pref[trips[i][1]] += trips[i][0]
            pref[trips[i][2]] -= trips[i][0]

        check = 0
        for i in range(len(pref)):
            check += pref[i]
            if check > capacity:
                return False
        
        return True
