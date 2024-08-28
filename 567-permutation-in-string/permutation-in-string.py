class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length_s1 = len(s1)
        length_s2 = len(s2)    

        count_s1 = Counter(s1)    

        # defining our range for the for-loop
        k = length_s2 - length_s1 + 1 

        # our for loop goes k times, based on the s1 length loops for the entire s2 string

        for i in range(k):
            count_s2 = Counter(s2[i : i + length_s1])

            if count_s1 == count_s2:
                return True
        
        return False
        
        # look into another solutions for more optimisations
