class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        length = len(trips)
        pref = [0] * (1001)

        for numPass, start, end in trips:
            pref[start] += numPass
            pref[end] -= numPass

        
        for i in range(1, len(pref)):
            pref[i] += pref[i - 1]      
        
        return max(pref) <= capacity
