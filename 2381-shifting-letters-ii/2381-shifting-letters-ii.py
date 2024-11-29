class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        length = len(s)
        pref = [0] * length

        for shift in shifts:
            start, end, val = shift
            if val == 0:
                pref[start] += -1
                if end + 1 < length:
                    pref[end + 1] -= -1
            else:
                pref[start] += 1
                if end + 1 < length:
                    pref[end + 1] -= 1
        
        a = list(accumulate(pref))
        res=""
        for i in range(length):
            res += chr((ord(s[i]) - ord('a') + a[i]) % 26  + ord("a"))
        
        return res
       


                
